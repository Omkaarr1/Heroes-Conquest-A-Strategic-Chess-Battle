import asyncio
import websockets
import json
from .game_logic import GameLogic
from .ai import AI

class WebSocketServer:
    def __init__(self):
        self.game_logic = GameLogic()
        self.ai = AI(self.game_logic)

    async def handler(self, websocket, path):
        async for message in websocket:
            data = json.loads(message)
            piece = data.get('piece')
            move = data.get('move')

            if self.game_logic.validate_move(piece, move):
                self.game_logic.apply_move(piece, move)
                lastMove = {
                    'player': 'A',
                    'piece': piece,
                    'move': move
                }
                self.game_logic.switch_turn()

                if self.game_logic.current_turn == 'B':
                    ai_move = self.ai.make_move()
                    if ai_move:
                        applied_piece = {
                            'piece': self.game_logic.board[ai_move['row']][ai_move['col']],
                            'row': ai_move['row'],
                            'col': ai_move['col']
                        }
                        self.game_logic.apply_move(applied_piece, ai_move['move'])
                        lastMove = {
                            'player': 'B',
                            'piece': applied_piece,
                            'move': ai_move['move']
                        }
                    self.game_logic.switch_turn()

                state, turn = self.game_logic.get_game_state()
                await websocket.send(json.dumps({
                    'board': state,
                    'turn': turn,
                    'lastMove': lastMove  # Send the last move to the client
                }))
            else:
                await websocket.send(json.dumps({
                    'invalid_move': True,
                    'message': 'Invalid move. Please try again.'
                }))

    def start(self):
        asyncio.get_event_loop().run_until_complete(
            websockets.serve(self.handler, 'localhost', 6789)
        )
        asyncio.get_event_loop().run_forever()

if __name__ == "__main__":
    server = WebSocketServer()
    server.start()

# Filename: server/websocket_server.py

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

            # Validate the player's move
            if self.game_logic.validate_move(piece, move):
                self.game_logic.apply_move(piece, move)
                self.game_logic.switch_turn()

                if self.game_logic.current_turn == 'B':
                    ai_move = self.ai.make_move()
                    if ai_move:
                        self.game_logic.apply_move(
                            {'piece': self.game_logic.board[ai_move['row']][ai_move['col']],
                             'row': ai_move['row'],
                             'col': ai_move['col']},
                            ai_move['move']
                        )
                    self.game_logic.switch_turn()

                # Send updated game state to the client
                state, turn = self.game_logic.get_game_state()
                await websocket.send(json.dumps({
                    'board': state,
                    'turn': turn
                }))
            else:
                # Send invalid move message to the client
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

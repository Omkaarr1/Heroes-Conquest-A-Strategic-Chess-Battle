# Filename: server/ai.py

import random

class AI:
    def __init__(self, game_logic):
        self.game_logic = game_logic

    def make_move(self):
        # AI selects a random piece and a valid move
        possible_moves = ['L', 'R', 'F', 'B', 'FL', 'FR', 'BL', 'BR']
        ai_pieces = [(4, col) for col in range(5) if self.game_logic.board[4][col] != '']
        
        if not ai_pieces:
            return None

        # Try several moves until a valid one is found
        for _ in range(100):
            piece = random.choice(ai_pieces)
            move = random.choice(possible_moves)
            if self.game_logic.validate_move({'row': piece[0], 'col': piece[1], 'piece': self.game_logic.board[piece[0]][piece[1]]}, move):
                return {'row': piece[0], 'col': piece[1], 'move': move}
        return None  # No valid move found

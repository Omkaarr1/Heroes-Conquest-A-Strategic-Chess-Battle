# Filename: server/game_logic.py

class GameLogic:
    def __init__(self):
        print("Initializing GameLogic")
        self.board = self.initialize_board()
        self.current_turn = 'A'  # Player A starts the game
        print("Initial board state:", self.board)

    def initialize_board(self):
        # Initialize the 5x5 board with players' pieces
        board = [['' for _ in range(5)] for _ in range(5)]
        # Add Player A's pieces
        board[0] = ['A-P1', 'A-H1', 'A-H2', 'A-H3', 'A-P2']
        # Add Player B's pieces (AI)
        board[4] = ['B-P1', 'B-H1', 'B-H2', 'B-H3', 'B-P2']
        return board

    def validate_move(self, piece, move):
        print("Validating move for piece:", piece, "with move:", move)
        piece_type = piece['piece'].split('-')[1]  # Get piece type (P1, H1, H2)
        new_position = self.calculate_new_position(piece['row'], piece['col'], move, piece_type)
        valid = self.is_within_bounds(new_position) and not self.is_friendly_fire(piece, new_position)
        print("Move validation result:", valid)
        return valid

    def apply_move(self, piece, move):
        print("Applying move for piece:", piece, "with move:", move)
        piece_type = piece['piece'].split('-')[1]  # Get piece type (P1, H1, H2)
        new_position = self.calculate_new_position(piece['row'], piece['col'], move, piece_type)

        # Check if new position is within bounds and the move is valid
        if self.is_within_bounds(new_position):
            # Remove piece from old position
            print(f"Removing piece from ({piece['row']}, {piece['col']})")
            self.board[piece['row']][piece['col']] = ''

            # Handle attacks (Hero1 and Hero2 can kill opponents in their path)
            if piece_type in ['H1', 'H2']:
                self.handle_attacks(piece, new_position)

            # Place piece in new position
            print(f"Placing piece at ({new_position['row']}, {new_position['col']})")
            self.board[new_position['row']][new_position['col']] = piece['piece']

            # Update piece's position for the next move
            piece['row'] = new_position['row']
            piece['col'] = new_position['col']
        else:
            print("Invalid move, not applying")

    def calculate_new_position(self, row, col, move, piece_type):
        if self.current_turn == 'A':  # Player A's moves
            if piece_type == 'P1':  # Pawn moves one block in any direction
                if move == 'L':
                    col -= 1
                elif move == 'R':
                    col += 1
                elif move == 'F':
                    row += 1  # Forward from the player's perspective is down the board
                elif move == 'B':
                    row -= 1  # Backward is up the board
            elif piece_type == 'H1':  # Hero1 moves two blocks straight
                if move == 'L':
                    col -= 2
                elif move == 'R':
                    col += 2
                elif move == 'F':
                    row += 2
                elif move == 'B':
                    row -= 2
            elif piece_type == 'H2':  # Hero2 moves two blocks diagonally
                if move == 'FL':
                    row += 2
                    col -= 2
                elif move == 'FR':
                    row += 2
                    col += 2
                elif move == 'BL':
                    row -= 2
                    col -= 2
                elif move == 'BR':
                    row -= 2
                    col += 2
        else:  # AI's moves (Player B)
            if piece_type == 'P1':  # Pawn moves one block in any direction
                if move == 'L':
                    col -= 1
                elif move == 'R':
                    col += 1
                elif move == 'F':
                    row -= 1  # Forward from the AI's perspective is up the board
                elif move == 'B':
                    row += 1  # Backward is down the board
            elif piece_type == 'H1':  # Hero1 moves two blocks straight
                if move == 'L':
                    col -= 2
                elif move == 'R':
                    col += 2
                elif move == 'F':
                    row -= 2
                elif move == 'B':
                    row += 2
            elif piece_type == 'H2':  # Hero2 moves two blocks diagonally
                if move == 'FL':
                    row -= 2
                    col -= 2
                elif move == 'FR':
                    row -= 2
                    col += 2
                elif move == 'BL':
                    row += 2
                    col -= 2
                elif move == 'BR':
                    row += 2
                    col += 2

        print("New position calculated:", {'row': row, 'col': col})
        return {'row': row, 'col': col}

    def handle_attacks(self, piece, new_position):
        # Check if there's an opponent at the new position and remove it
        target_piece = self.board[new_position['row']][new_position['col']]
        if target_piece and not target_piece.startswith(self.current_turn):
            print(f"{piece['piece']} attacks and removes {target_piece} at ({new_position['row']}, {new_position['col']})")
            self.board[new_position['row']][new_position['col']] = ''  # Remove the opponent piece

    def is_friendly_fire(self, piece, new_position):
        # Check if the new position is occupied by a friendly piece
        target_piece = self.board[new_position['row']][new_position['col']]
        friendly_fire = target_piece.startswith(self.current_turn)
        if friendly_fire:
            print(f"Friendly fire detected: {piece['piece']} cannot move to ({new_position['row']}, {new_position['col']}) occupied by {target_piece}")
        return friendly_fire

    def is_within_bounds(self, position):
        # Ensure the row and col are within the 5x5 grid
        within_bounds = 0 <= position['row'] < 5 and 0 <= position['col'] < 5
        print("Position", position, "is within bounds:", within_bounds)
        return within_bounds

    def get_game_state(self):
        # Return the current game state
        print("Returning current game state")
        return self.board, self.current_turn

    def switch_turn(self):
        print("Switching turn from", self.current_turn)
        self.current_turn = 'B' if self.current_turn == 'A' else 'A'
        print("Turn switched to", self.current_turn)

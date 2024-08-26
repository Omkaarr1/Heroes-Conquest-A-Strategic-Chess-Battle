# 🛡️ Heroes' Conquest: A Strategic Chess Battle

Welcome to **Heroes' Conquest: A Strategic Chess Battle**, a unique and advanced chess-like game that offers a fresh twist on traditional chess mechanics. Engage in a turn-based strategy game where you command a set of powerful heroes and pawns, each with distinct abilities, to outmaneuver and defeat your opponent.

## 🌟 Features

### 🎮 Intuitive Game Interface
- **Dynamic Game Board:** A 5x5 grid where each cell represents a possible position for your pieces.
- **Interactive Controls:** Easy-to-use buttons for selecting piece movements in all directions.
- **Real-time Feedback:** The game state is updated in real-time, with clear indicators for the current player, selected piece, and chosen move.

### 🧠 Advanced Game Logic
- **Unique Pieces:**
  - **Pawn (P):** Moves 1 step in any direction.
  - **Hero1 (H1):** Moves 2 steps in any straight direction.
  - **Hero2 (H2):** Moves 2 steps diagonally.
  - **Hero3 (H3):** Moves 2 steps in one direction, then 1 step perpendicular.
- **Strategic AI Opponent:** Face off against an AI that makes random but valid moves to challenge your strategic thinking.
- **Move Validation:** All moves are validated to ensure they are within bounds and not resulting in friendly fire.

### 📜 Detailed Move History
- **Track Your Progress:** Every move you and the AI make is recorded in a move history panel, allowing you to review your strategic decisions.

### 🥇 Win Conditions
- **Clear Victory Paths:** The game checks for a winner after every move, ensuring a clear path to victory.
  - Win by eliminating all of your opponent's pieces.
  - Win by reaching the opposite end of the board with one of your pieces.

## 🚀 Getting Started

### Prerequisites
- Python 3.x
- Web browser (for playing the game)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/heroes-conquest.git
   cd heroes-conquest
   ```
2. **Install dependencies:**
   ```bash
   Copy code
   pip install websockets
   Run the WebSocket server:
   ```
3. Goto http://localhost:8000 to access the game.

## 📖 How to Play

### Starting the Game:
- Player A (You) begins the game. The board will be initialized with Player A's pieces on the top row and Player B's (AI) pieces on the bottom row.

### Selecting a Piece:
- Click on any of your pieces (marked with an "A-") on the board. The piece's name will be displayed in the "Selected" section.

### Choosing a Move:
- Use the direction buttons to choose where you want to move your selected piece. The possible directions include:
  - Left (L)
  - Right (R)
  - Forward (F)
  - Backward (B)
  - Diagonal moves: Forward-Left (FL), Forward-Right (FR), Backward-Left (BL), Backward-Right (BR).

### Submitting Your Move:
- Once you've selected both the piece and the move, click the "Submit Move" button. Your move will be sent to the server, and the AI will then take its turn.

### Game Progression:
- The game alternates turns between Player A and Player B (AI). The current player's turn is always displayed on the interface.

### Winning the Game:
- The game will automatically check for victory conditions after each move:
  - **Elimination:** Win if you remove all of your opponent's pieces from the board.
  - **End Reach:** Win if any of your pieces reaches the opponent's starting row.

## 🛡️ Piece Movement Guide
- **Pawn (P):** Moves 1 step in any direction (⬆️⬇️⬅️➡️).
- **Hero1 (H1):** Moves 2 steps in any straight direction (⬆️⬇️⬅️➡️).
- **Hero2 (H2):** Moves 2 steps diagonally (↖️↗️↙️↘️).
- **Hero3 (H3):** Moves 2 steps in one direction, then 1 step perpendicular (All directions).

## 🏆 Deciding the Winner
The game ends when one of the following conditions is met:

1. **Piece Elimination:** If all pieces of one player are removed from the board, the opponent wins.
2. **Reach Opponent's End:** If a piece reaches the opposite end of the board (the starting row of the opponent), the player who made the move wins.

The winner is announced immediately, and the game can be restarted for another round of strategic fun!

## 👥 Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request. Let's make **Heroes' Conquest** even better together!

## 📧 Contact
If you have any questions or suggestions, feel free to reach out to me at [omkargupta702@gmail.com](mailto:omkargupta702@gmail.com).

**Enjoy the game, and may the best strategist win!**



# 🔴 Checkers AI (Human vs. Minimax Engine) 🚀

Welcome to **Checkers AI**—a fully interactive, smooth-rendering Checkers game built from scratch using **Python** and **Pygame**. 

What started as a classic local two-player game has been upgraded with a **Minimax Algorithm brain**, transforming it into a high-stakes battle between human intuition and machine calculation!

---

## 🧠 The AI Intellect: Basic Minimax Engine
No randomness here. The computer utilizes a **Minimax Decision Tree Algorithm** to peer into the immediate future. 
* It simulates every possible valid move on a virtual board.
* It predicts your best counter-moves.
* It calculates an optimal scoring strategy based on piece counts, king counts, and positioning to crush its opponent.

---

## 🛠️ Project Architecture
<img width="1010" height="1022" alt="Recording 2026-06-03 163505" src="https://github.com/user-attachments/assets/8bd39eae-e3c3-4695-a24b-79747df1ce47" />

The codebase is built using a highly organized, object-oriented approach keeping game logic completely separated from the rendering engine:

* **`main.py`** – The Grand Central Station. Handles the Pygame window, the clock frame rates, mouse events, and orchestrates the turn loop between human and AI.
* **`minimax.py`** – The AI Core. Executes the recursive look-ahead tree logic to determine the maximizing score for the computer.
* **`checkers/board.py`** – The Game State. Manages the 8x8 grid matrix, draws squares, handles jumping physics, piece removal, and scores the current board state.
* **`checkers/game.py`** – The Ref. Tracks whose turn it is, updates valid move indicators on the fly, and registers wins/losses.
* **`checkers/piece.py`** – The Soldiers. Handles rendering normal tokens, managing coordinate geometry, and crowning pieces when they reach the back row.

---

## 🕹️ Features

* 🎯 **Visual Move Indicators:** Clicking a piece instantly highlights all legal moves and potential multi-jump paths with clean visual anchors.
* 👑 **Automatic King Promotion:** Reaching the opposite end transforms your piece into a King, unlocking bidirectional movement.
* 🤖 **Instant AI Response:** Configured at an optimal depth tree to ensure the AI responds with calculated decisions instantly without breaking a sweat or lagging your system.
* 🏆 **Built-in Game Over Sequence:** Elegant end-game screens overlaying the board to declare the ultimate winner.

---

## 💻 Getting Started

### Prerequisites

⚡ Future Upgrades on the Horizon
While the current build relies on a pure, elegant baseline Minimax model, future expansions could include:

1. Alpha-Beta Pruning to cut off dead-end decision branches and boost calculation speed.
2. Positional Weight Matrices to reward center-board control and back-row defense strategies.
3. Move History Stack to allow a custom "Undo Move" feature.

Made with 🧠, Python, and a love for classic board games. Feel free to fork, tweak, and test your strategy against the machine!


Make sure you have Python installed, then grab **Pygame**:
pip install pygame




# ❄️ Snowman Meltdown

Snowman Meltdown is a Python command‑line word guessing game inspired by Hangman.  
Instead of a gallows, a snowman slowly melts away with each wrong guess.  
The goal: guess the secret word before the snowman disappears!

---

## 📂 Project Structure

Snowman-Meltdown/
```bash
tree .

├── ascii_art.py
├── game_logic.py
├── main.py
├── snowman.py
└── test_game_logic.py
└── README.md # Project documentation

2 directories, 6 files
```

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/etherblitzdev/Snowman-Meltdown.git
cd Snowman-Meltdown
```

### 2. Create and activate a virtual environment
```bash
python3 -m venv snowman-env
source snowman-env/bin/activate   # macOS/Linux

python -m venv snowman-env
snowman-env\Scripts\activate      # Windows
```

### 3. Install dependencies
```bash
pip install pytest
```

### 4. 🎮 Play the Game - Run the entry point:
```bash
python3 snowman.py
```

### 5. 🧪 Running Tests - Unit tests are included for core functions.
```bash
pytest -v
```

🛠 Development Notes:

    •   Modular design: ASCII art (ascii_art.py) and game logic (game_logic.py) are separated for maintainability.
    
    •   Override‑safe imports: snowman.py imports only play_game() from game_logic.py.
    
    •   Testing focus: test_game_logic.py validates word selection and display formatting.

📌 Roadmap:

    •   Add more word categories (animals, tech, geography).

    •   Improve test coverage (win/lose scenarios, invalid input handling).

    •   Optional difficulty levels (easy/medium/hard).

    •   Future support for multiplayer or web UI.

## 📄 License

MIT License

Copyright (c) 2025 etherblitzdev

This project is licensed under the MIT License.  
See [LICENSE](LICENSE) for details.

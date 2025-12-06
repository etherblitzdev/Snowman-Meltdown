
# ❄️ Snowman Meltdown

Snowman Meltdown is a Python command‑line word guessing game inspired by Hangman.  
Instead of a gallows, a snowman slowly melts away with each wrong guess.  
The goal: guess the secret word before the snowman disappears!

---

## 📂 Project Structure

Snowman-Meltdown/
```bash
tree .
├── ascii_art.py        # Snowman melting stages
├── game_logic.py       # Core gameplay loop, input validation, replay logic
├── main.py             # Entry point that calls game_logic.main()
├── snowman.py          # (legacy stub, can be removed or kept for reference)
├── test_game_logic.py  # Pytest unit tests
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

### 3. Freeze the environment
Use pip freeze to list all installed packages with their versions:

```bash
pip freeze > requirements.txt
```

### 4. Check the file:
Open requirements.txt
```bash
astroid==4.0.2
black==25.11.0
click==8.3.1
dill==0.4.0
iniconfig==2.3.0
isort==7.0.0
mccabe==0.7.0
mypy_extensions==1.1.0
packaging==25.0
pathspec==0.12.1
platformdirs==4.5.1
pluggy==1.6.0
Pygments==2.19.2
pylint==4.0.4
pytest==9.0.1
pytokens==0.3.0
ruff==0.14.8
tomlkit==0.13.3
```

### 5. 🎮 Play the Game - Run the entry point:
```bash
python3 main.py
```

### 6. 🧪 Running Tests - Unit tests are included for core functions.
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

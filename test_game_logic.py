# test_game_logic.py
import pytest
from game_logic import display_game_state, get_random_word

def test_get_random_word_returns_valid_word():
    word = get_random_word()
    assert isinstance(word, str)
    assert len(word) > 0

def test_display_game_state_runs_without_error(capsys):
    secret_word = "snowman"
    guessed_letters = ["s", "n"]
    mistakes = 0
    display_game_state(mistakes, secret_word, guessed_letters)
    captured = capsys.readouterr()
    assert "Word:" in captured.out
    assert "s _ _ n _ _ n" in captured.out or "s _ _ _ _ _ n" in captured.out

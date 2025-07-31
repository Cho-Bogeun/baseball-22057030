import pytest

from game import Game
from game_result import GameResult


@pytest.fixture
def game():
    return Game()


def assert_illegal_argument(game, guess):
    with pytest.raises(TypeError):
        game.guess(guess)

@pytest.mark.parametrize("invalid_inputs", [None, "12", "1234", "12s", "121"])
def test_exception_when_invalid_argument(game, invalid_inputs):
    assert_illegal_argument(game, invalid_inputs)

def test_return_solved_if_matched_numbers(game):
    game.question = "123"
    result: GameResult = game.guess("123")

    assert result is not None
    assert result.solved == True
    assert result.strikes == 3
    assert result.balls == 0
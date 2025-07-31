import pytest

from game import Game

@pytest.fixture
def game():
    return Game()


def assert_illegal_argument(game, guess):
    with pytest.raises(TypeError):
        game.guess(guess)

@pytest.mark.parametrize("invalid_inputs", [None, "12", "1234", "12s", "121"])
def test_exception_when_invalid_argument(game, invalid_inputs):
    assert_illegal_argument(game, invalid_inputs)
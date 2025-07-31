import pytest

from game import Game


def test_exception_with_input_is_none():
    game = Game()

    with pytest.raises(TypeError):
        game.guess(None)
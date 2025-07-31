import pytest

from game import Game
from game_result import GameResult


@pytest.fixture
def game():
    return Game()


def assert_illegal_argument(game, guess):
    with pytest.raises(TypeError):
        game.guess(guess)

def assert_matched_number(result, solved, strikes, balls):
    assert result is not None
    assert result.solved == solved
    assert result.strikes == strikes
    assert result.balls == balls

@pytest.mark.parametrize("invalid_inputs", [None, "12", "1234", "12s", "121"])
def test_exception_when_invalid_argument(game, invalid_inputs):
    assert_illegal_argument(game, invalid_inputs)


def test_return_solved_if_matched_numbers(game):
    game.question = "123"
    assert_matched_number(game.guess("123"), solved=True, strikes=3, balls=0)


def test_return_solved_if_unmatched_numbers(game):
    game.question = "123"
    assert_matched_number(game.guess("456"), solved = False, strikes=0, balls=0)

def test_strikes_if_2_strikes_0_ball(game):
    game.question = "123"
    result = game.guess("124")

    assert result.strikes == 2

def test_strikes_if_1_strikes_2_ball(game):
    game.question = "123"
    result = game.guess("132")

    assert result.strikes == 1
    assert result.balls == 2
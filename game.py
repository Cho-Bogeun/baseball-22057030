from game_result import GameResult


class Game:
    def __init__(self):
        self._question = ""

    @property
    def question(self):
        raise AttributeError

    @question.setter
    def question(self, value):
        self._question = value

    def guess(self, numbers):
        self._assert_illegal_value(numbers)
        if self._question == numbers:
            return GameResult(True, 3, 0)

        strike_list = [n for q,n in zip(self._question, numbers) if q==n]
        ball_list = [n for n in numbers if (n in set(self._question) and n not in strike_list)]
        return GameResult(False, len(strike_list), len(ball_list))

    def _assert_illegal_value(self, numbers):
        if numbers is None:
            raise TypeError("입력이 없음")
        
        if len(numbers) != 3:
            raise TypeError("세글자가 아님")
        
        if not numbers.isdigit():
            raise TypeError("숫자가 아님")
            
        if self._does_duplicated(numbers):
            raise TypeError("중복 숫자 존재")

    def _does_duplicated(self, numbers):
        return len(set(numbers)) != 3
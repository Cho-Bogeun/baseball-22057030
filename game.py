class Game:
    def guess(self, numbers):
        self._assert_illegal_value(numbers)

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
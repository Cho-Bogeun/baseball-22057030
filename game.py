class Game:
    def guess(self, numbers):
        if numbers is None:
            raise TypeError()

        if len(numbers) != 3:
            raise TypeError

        for number in numbers:
            if not ord("0") <= ord(number) <= ord("9"):
                raise TypeError
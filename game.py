class Game:
    def guess(self, number):
        if number is None:
            raise TypeError()

        if len(number) != 3:
            raise TypeError
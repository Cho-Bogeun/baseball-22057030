class Game:
    def guess(self, number):
        if number is None:
            raise TypeError()
from random import choice


class Cards:
    """Случайный выбор игральной карты"""

    def __init__(self):
        self.index = 0
        self._SUITS = ['черви', 'бубны', 'пики', 'крести']
        self._RANKS = [*range(2, 11), 'J', 'Q', 'K', 'A']

    def __next__(self):
        suit = choice(self._SUITS)
        rank = choice(self._RANKS)
        return f'({rank}, {suit})'

    def __iter__(self):
        return self


deck = Cards()
print(next(deck))


# ДОБАВИТЬ: закомментированный вывод результатов нескольких запусков скрипта с различными входными данными (при наличии)
# tests:

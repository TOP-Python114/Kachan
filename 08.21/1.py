from random import choice,shuffle


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


def displace_str(array):
    """Функция-генератор, принимающая на вход множество set, и возвращающую в строковом виде перестановки для элементов этого множества"""
    #array_new = []
    #counter_1 = 0
    #counter_2 = 0
    array = list(array)
    if not array:
        yield array
    else:
        for counter_1 in range(len(array)):
            array_new = array[:counter_1] + array[counter_1 + 1:]
            for counter_2 in displace_str(array_new):
                yield array[counter_1: counter_1 + 1] + counter_2


for elem in displace_str({'a','b', 'c'}):
    print(''.join(''.join(elem)))


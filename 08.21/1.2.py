
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


from time import perf_counter_ns, sleep


def function_of_time(func):
    """Декоратор для оценки времени выполнения функции.
    Используйте модуль time, функции perf_counter и perf_counter_ns"""

    def wrapped(*args):
        start_time = perf_counter_ns()
        result = (perf_counter_ns() - start_time)
        res = func(*args)
        print(f'Время выполнения: {result}')
        return res
    return wrapped


@function_of_time
def func(a, b):
    return a + b


add_func = func(100, 50)
print(f'Результат сложения: {add_func}')




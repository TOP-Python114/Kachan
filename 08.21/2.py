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


def log_errors(func_new):

    """Декоратор, который который логирует вызов функции в файл-журнал, используя атрибуты объекта функции __name__ и аргументы, переданные функции"""

    def wrapper(a, b):
        result = func_new(a, b)
        file_name = 'function_errors.log'
        file = open(file_name, mode='a')
        file.write(f'Функция: {func_new.__name__} \n {a} \n {b} \n')
        return result
    return wrapper


@log_errors
def checkhand(a, b):

    return a - b


print(checkhand(10, 0))



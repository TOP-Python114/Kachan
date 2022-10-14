from time import perf_counter_ns, sleep


# ИСПРАВИТЬ: имена — что такое function_of_time и func?
# ДОБАВИТЬ: аннотации типов параметров и возвращаемого значения
def function_of_time(func):
    # ИСПРАВИТЬ: документация функции/метода начинается с глагола и в одно предложение отвечает на вопрос "что делает функция/метод?"
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


# ДОБАВИТЬ: закомментированный вывод результатов нескольких запусков скрипта с различными входными данными (при наличии)
# tests:

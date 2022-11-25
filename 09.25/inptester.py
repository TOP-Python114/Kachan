"""
Предоставляет функцию быстрого доступа и настраиваемый класс для проверки вызываемых объектов с помощью ручного ввода в stdin.

2022 Геннадий Шаповаленко
"""

from typing import Callable
from enum import Enum


class Label(str, Enum):
    PROMPT = 'введите строку'
    ERROR = 'неверный ввод'
    QUIT = ''


class InputTester:
    def __init__(self,
                 prompt_string: str,
                 error_string: str,
                 function_object: Callable,
                 quit_string: str = Label.QUIT,
                 **function_kwargs):
        self.prompt = f"\n > {prompt_string}: "
        self.error = f" _ {error_string} _ "
        self.quit = quit_string
        self.function = function_object
        self.kwargs = function_kwargs
        self.results: list = []

    def start(self, *validators: Callable, str_to_int: bool = False) -> list:
        """Запускает условно-бесконечный цикл для обработки ввода. Цикл прерывается по вводу пустой строки (по умолчанию) либо значения, равного self.error. Возвращает список объектов, которые вернула self.function() на каждой итерации.

        :param validators: предикативные функции с одним обязательным аргументом для проверки корректности ввода
        :param str_to_int: преобразование ввода в int объект (с независимой валидацией)
        :return: список всех возвращённых значений self.function()
        """
        while True:
            err_flag = False
            inp = input(self.prompt)
            if inp == self.quit:
                break

            try:
                if str_to_int:
                    inp = int(inp)
            except ValueError:
                err_flag = True
            else:
                if all(func(inp) for func in validators):
                    self.results += [self.function(inp, **self.kwargs)]
                else:
                    err_flag = True
            finally:
                if err_flag:
                    print(self.error)

        return self.results


def inptester(func_obj: Callable, *validators: Callable, str_to_int: bool = False, **func_kwargs) -> list:
    """Осуществляет быстрый запуск stdin теста функции func_obj(). Тест прерывается по вводу пустой строки. Возвращает список объектов, которые вернула func_obj() на каждой итерации.
    InputTester инициализируется значениями по умолчанию.

    :param func_obj: вызываемый объект, для передачи в него ввода
    :param func_kwargs: словарь дополнительных ключевых аргументов для вызываемого объекта
    :param validators: предикативные функции с одним обязательным аргументом для проверки корректности ввода
    :param str_to_int: преобразование ввода в int объект (с независимой валидацией)
    :return: список всех возвращённых значений func_obj()
    """
    it = InputTester(
        prompt_string=Label.PROMPT,
        error_string=Label.ERROR,
        quit_string=Label.QUIT,
        function_object=func_obj,
        **func_kwargs)
    return it.start(*validators, str_to_int=str_to_int)



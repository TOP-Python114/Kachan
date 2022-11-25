from typing import Optional

###############################################################################
# вариант 1
class Handler:
    """Класс обработчика"""
    def handle(self, code):
        raise NotImplementedError()


class Http404Handler(Handler):
    """Обработчик для кода 404"""
    def handle(self, code) -> str:
        if code == 404:
            return 'Страница не найдена'


class Http401Handler(Handler):
    """Обработчик для кода 401"""
    def handle(self, code) -> str:
        if code == 401:
            return 'Неавторизированный запрос'


class Http200Handler(Handler):
    """Обработчик для кода 200"""
    def handle(self, code) -> str:
        if code == 200:
            return 'Запрос выполнен успешно'

class Http403Handler(Handler):
    """Обработчик для кода 403"""
    def handle(self, code) -> str:
        if code == 403:
            return 'Доступ к ресурсу запрещен'

class Http500Handler(Handler):
    """Обработчик для кода 500"""
    def handle(self, code) -> str:
        if code == 500:
            return 'Ошибка сервера'


class Client:
    """Класс клиент"""
    def __init__(self):
        self.__handlers = []

    def add_handler(self, item) -> None:
        self.__handlers.append(item)

    def answer(self, code) -> str:
        for item in self.__handlers:
            msg = item.handle(code)
            # ИСПРАВИТЬ: в таких ситуациях лучше явно проверять, является ли возвращённое значение объектом None — чтобы не спутать с пустой строкой или любым другим объектом, приводящимся к False
            if msg:
                # ИСПРАВИТЬ: заявлено возвращаемое значение str, но здесь строка не возвращается, а выводится в стандартный поток stdout — это разные явления — возвращается же фактически всегда None
                print(msg)
                break
        else:
            print(f'Запрос не авторизирован')


client = Client()
client.add_handler(Http401Handler())
client.add_handler(Http403Handler())
client.add_handler(Http404Handler())
client.add_handler(Http200Handler())
client.add_handler(Http500Handler())

i = 0
while i < 10:
    code = int(input('Введите код ошибки\n'))
    client.answer(code)
    i += 1

# ИСПОЛЬЗОВАТЬ: вообще, для таких ручных тестов пишут условно-бесконечную обработку ввода, пока не будет введена пустая строка или строка, по которой будет осуществлён выход — а здесь любой некорректный ввод вызывает прерывание работы приложения, что неудобно для последовательных тестов
# while True:
#     inp = input()
#     if not inp:
#         break
#     if inp.isdecimal():
#         client.answer(inp)
#     else:
#         print('некорректный ввод')

# ИСПОЛЬЗОВАТЬ: не говоря уже о том, что можно один раз написать небольшое, относительно универсальное приложение для ручного тестирования, разместить файл с ним в библиотеке глобального интерпретатора или виртуального окружения, а затем импортировать этот модуль везде, где требуется ручной тест
# from inptester import inptester
# inptester(client.answer, str_to_int=True)


# Введите код ошибки
# 500
# Ошибка сервера
# Введите код ошибки
# 5
# Запрос не авторизирован
# Введите код ошибки
# 8
# Запрос не авторизирован
# Введите код ошибки
# 401
# Неавторизированный запрос
# Введите код ошибки
# 403
# Доступ к ресурсу запрещен
# Введите код ошибки
# 800
# Запрос не авторизирован
# Введите код ошибки
# 401
# Неавторизированный запрос
# Введите код ошибки
# 403
# Доступ к ресурсу запрещен
# Введите код ошибки
# 404
# Страница не найдена
# Введите код ошибки
# 500
# Ошибка сервера


###############################################################################
# вариант 2

class Handler:
    """Класс цепочки, запускает обработку данных."""
    def __init__(self):
        self.previous_modifier: Optional[Handler] = None
        self.next_modifier: Optional[Handler] = None

    def add_modifier(self, modifier: 'Handler'):
        """Формирует звено цепочки."""
        if self.next_modifier is None:
            self.next_modifier = modifier
            self.next_modifier.previous_modifier = self
        else:
            self.next_modifier.add_modifier(modifier)

    def handle(self, code):
        if self.next_modifier:
            self.next_modifier.handle(code)


class Http404Handler(Handler):
    """Обработчик для кода 404"""
    # ОТВЕТИТЬ: что такое стандартный поток? чем отличается возврат строки функцией/методом от вывода строки в stdout?
    # ИСПРАВИТЬ здесь и далее: привести в соответствие аннотацию возвращаемого значения с фактически возвращаемым
    def handle(self, code) -> str:
        if code == 404:
            print(f'Страница не найдена')
        super().handle(code)


class Http401Handler(Handler):
    """Обработчик для кода 401"""
    def handle(self, code) -> str:
        if code == 401:
            print(f'Неавторизированный запрос')
        super().handle(code)


class Http200Handler(Handler):
    """Обработчик для кода 200"""
    def handle(self, code) -> str:
        if code == 200:
            print(f'Запрос выполнен успешно')
        super().handle(code)


class Http403Handler(Handler):
    """Обработчик для кода 403"""
    def handle(self, code) -> str:
        if code == 403:
            print(f'Доступ к ресурсу запрещен')
        super().handle(code)


class Http500Handler(Handler):
    """Обработчик для кода 500"""
    def handle(self, code) -> str:
        if code == 500:
            print(f'Ошибка сервера')
        super().handle(code)


root = Handler()
root.add_modifier(Http500Handler())
root.add_modifier(Http200Handler())
root.add_modifier(Http401Handler())
root.add_modifier(Http404Handler())
root.add_modifier(Http403Handler())

i = 0
while i < 6:
    code = int(input('Введите код ошибки\n'))
    root.handle(code)
    i += 1


# Введите код ошибки
# 500
# Ошибка сервера
# Введите код ошибки
# 200
# Запрос выполнен успешно
# Введите код ошибки
# 403
# Доступ к ресурсу запрещен
# Введите код ошибки
# 401
# Неавторизированный запрос
# Введите код ошибки
# 200
# Запрос выполнен успешно
# Введите код ошибки
# 500
# Ошибка сервера


# ОТВЕТИТЬ: и какой вариант удобнее по-вашему?


# ИТОГ: порадовали двумя вариантами, реализованы оба хорошо, осталось с возвращаемыми/выводимыми значениями разобраться — 10/12

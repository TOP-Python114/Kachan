#У вас есть веб-сервер, принимающий и обрабатывающий запросы. Каждый запрос после обработки получает ответ с определённым кодом.
#Этот ответ должен пройти цепочку обработчиков, каждый из которых реагирует только на один определённый код.
#Напишите класс, имитирующий получение веб-сервером запросов (например, из stdin) и генерацию ответов с кодами (например: 200, 403, 404, 500).
#Ответ может быть кортежем, словарём, отдельным классом или любой другой структурой данных — главное, чтобы одним из элементов этой структуры был код ответа.
#Напишите классы-обработчики в количестве, соответствующем числу генерируемых вариантов кодов ответа.
#Каждый обработчик должен проверять код ответа.
#Если код в ответе не соответствует коду конкретного обработчика, то обработчик ничего не делает с ответом, а передаёт объект ответа дальше (работа цепочки продолжается).
#Если код в ответе эквивалентен коду конкретного обработчика, то обработчик должен обозначить свою реакцию (например, сообщением в stdout, содержащим имя класса обработчика) и НЕ должен передавать объект дальше (работа цепочки останавливается).
#Самостоятельно выберите способ реализации: цепочка методов или брокер событий + CQS.
from typing import Optional
#вариант 1
class Handler:
    """Класс обработчика"""
    def handle(self, code):
        raise NotImplementedError()


class Http404handler(Handler):
    """Обработчик для кода 404"""
    def handle(self, code) -> str:
        if code == 404:
            return 'Страница не найдена'

class Http401handler(Handler):
    """Обработчик для кода 401"""
    def handle(self, code) -> str:
        if code == 401:
            return 'Неавторизированный запрос'


class Http200handler(Handler):
    """Обработчик для кода 200"""
    def handle(self, code) -> str:
        if code == 200:
            return 'Запрос выполнен успешно'

class Http403handler(Handler):
    """Обработчик для кода 403"""
    def handle(self, code) -> str:
        if code == 403:
            return 'Доступ к ресурсу запрещен'

class Http500handler(Handler):
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
            if msg:
                print(msg)
                break
        else:
            print(f'Запрос не авторизирован')


client = Client()
client.add_handler(Http401handler())
client.add_handler(Http403handler())
client.add_handler(Http404handler())
client.add_handler(Http200handler())
client.add_handler(Http500handler())
i = 0
while i < 10:
    code = int(input('Введите код ошибки \n'))
    client.answer(code)
    i += 1
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
#################################################################################
#вариант 2

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


class Http404handler(Handler):
    """Обработчик для кода 404"""
    def handle(self, code) -> str:
        if code == 404:
            print(f'Страница не найдена')
        super().handle(code)

class Http401handler(Handler):
    """Обработчик для кода 401"""
    def handle(self, code) -> str:
        if code == 401:
            print(f'Неавторизированный запрос')
        super().handle(code)

class Http200handler(Handler):
    """Обработчик для кода 200"""
    def handle(self, code) -> str:
        if code == 200:
            print(f'Запрос выполнен успешно')
        super().handle(code)

class Http403handler(Handler):
    """Обработчик для кода 403"""
    def handle(self, code) -> str:
        if code == 403:
            print(f'Доступ к ресурсу запрещен')
        super().handle(code)

class Http500handler(Handler):
    """Обработчик для кода 500"""
    def handle(self, code) -> str:
        if code == 500:
            print(f'Ошибка сервера')
        super().handle(code)


root = Handler()
root.add_modifier(Http500handler())
root.add_modifier(Http200handler())
root.add_modifier(Http401handler())
root.add_modifier(Http404handler())
root.add_modifier(Http403handler())
i = 0
while i < 6:
    code = int(input('Введите код ошибки \n'))
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
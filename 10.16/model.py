"""Модель MVC."""

# ОТВЕТИТЬ: зачем здесь __future__? вы работает на версии младше 3.10? до сих пор вроде обходились как-то
from __future__ import annotations
from re import fullmatch


class Email:
    """Описывает модель взаимодействия и хранения email адресов."""
    file_path = 'emails.txt'

    def __init__(self, email: str):
        self.email = email

    @property
    def email(self) -> str:
        """Возвращает значение поля __email."""
        return self.__email

    @email.setter
    def email(self, value: str):
        """Проверяет, является ли переданная строка корректным email адресом, и устанавливает значение поля __email."""
        pattern = r'\b[a-zA-Z0-9_.-]+@[a-zA-Z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if fullmatch(pattern, value):
            self.__email = value
        else:
            raise ValueError(f'Invalid email address: {value}')

    def save(self) -> None:
        """Добавляет значение поля __email в файл."""
        with open(self.file_path, 'a', encoding='utf-8') as fileout:
            fileout.write(self.email + '\n')


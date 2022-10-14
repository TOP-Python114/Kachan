from typing import Optional
from datetime import datetime as dt
from sys import exit
from time import sleep


class Command:
    """Объект команды хранит в атрибутах имя и аргументы команды, позволяет выполнять команду и возвращать строку с результатом выполнения команды."""

    def __init__(self, command: str, args: str):
        self.command = command
        self.args = args
        self.history = {}

    def __str__(self):
        """Выводит словарь, содержащий команды."""
        return self.history

    def add(self) -> dict[str, str]:
        """Добавляет команду в словарь."""
        self.history[self.command] = self.args
        return self.history

    def execute(self) -> str:
        """Возвращает результат выполнения команды."""
        self.result = f'Операция {self.command} {self.args} успешно выполнена'
        return self.result


class BraNSh:
    """Объект оболочки для выполнения команд хранит историю последних выполненных команд, журналирует выполняемые команды."""

    __count = 0

    def __init__(self, command: Optional[Command]):
        self.command = command.command
        self.args = command.args
        self.todo = False

    def start(self) -> None:
        """Запускает обработку команд."""
        self.todo = True

    def get_commands(self) -> Optional[str]:
        """Обрабатывает ввод команд и их аргументов."""
        if self.command == 'exit':
            return self.exit()
        elif self.command == 'help':
            return self.help()
        elif self.command == 'log':
            self.__log()
        else:
            raise TypeError(f'Неизвестная команда')

    def help(self) -> str:
        """Возвращает строку со справкой по использованию объекта оболочки."""

    def __log(self) -> str:
        """Логирует выполняемые команды."""
        self.__class__.__count += 1
        if self.__class__.__count < 51:
            file_name = 'log_command_f.txt'
            file = open(file_name, mode='a')
            log_data = f'{dt.now()} {self.command} {self.args}'
            file.write(f'{log_data}\n')
            return log_data
        else:
            self.__class__.__count = 1
            file_name = 'log_command_f.txt'
            file = open(file_name, mode='w')
            log_data = f'{dt.now()} {self.command} {self.args}'
            file.write(f'{log_data}\n')
            return log_data

    def exit(self) -> None:
        """Завершает обработку команд."""
        self.todo = False
        print(self.command)
        exit


command_programs = Command('log', 'Запись')
do_command_programs = BraNSh(command_programs)
print(do_command_programs.__log())

sleep(5)

command_programs = Command('help', 'Помощь')
do_command_programs = BraNSh(command_programs)
print(do_command_programs.__log())

command_programs = Command('exit', 'Выход')
do_command_programs = BraNSh(command_programs)
print(do_command_programs.__log())

command_programs = Command('help', 'Помощь')
do_command_programs = BraNSh(command_programs)
print(do_command_programs.__log())

command_programs = Command('exit', 'Выход')
do_command_programs = BraNSh(command_programs)
print(do_command_programs.__log())

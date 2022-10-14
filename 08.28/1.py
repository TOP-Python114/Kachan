import sys
import datetime
import time
from typing import Optional


class Commands:
    """Оболочка командного интерпретатора"""

    def __init__(self, command: str, args: str):
        self.command = command
        self.args = args
        self.commands_dict = {}

    def __str__(self):
        return self.commands_dict

    def add_command(self):
        """Добавление команд в словарь"""
        self.commands_dict[self.command] = self.args
        return self.commands_dict

    def command_result(self):
        """вывод результата"""
        self.result = f'Операция {self.command} {self.args} успешно выполнена'
        return self.result


class BraNSh:
    """Инициализация логирования, начала работы"""

    _count = 0

    def __init__(self, command: Optional[Commands]):
        self.command = command.command
        self.args = command.args
        self.todo = False

    def start(self):
        """начало работы программы"""
        self.todo = True

    def work_commands(self):
        """выполнение команд"""
        if self.command == 'exit':
            return self.exit()
        elif self.command == 'help':
            return self.help()
        elif self.command == 'log':
            self.log()
        else:
            raise TypeError(f'Неизвестная команда')

    def help(self):
        """вывод справки"""

    def log(self):
        """логирование и запись в файл"""
        self.__class__._count += 1
        if self.__class__._count < 51:
            file_name = 'log_command_f.txt'
            file = open(file_name, mode='a')
            log_data = f'{datetime.datetime.now()} {self.command} {self.args}'
            file.write(f'{log_data}\n')
            return log_data
        else:
            self.__class__._count = 1
            file_name = 'log_command_f.txt'
            file = open(file_name, mode='w')
            log_data = f'{datetime.datetime.now()} {self.command} {self.args}'
            file.write(f'{log_data}\n')
            return log_data

    def exit(self):
        """выход из программы"""
        self.todo = False
        print(self.command)
        sys.exit


command_programms = Commands('log', 'Запись')
do_command_programms = BraNSh(command_programms)
print(do_command_programms.log())

time.sleep(5)

command_programms = Commands('help', 'Помощь')
do_command_programms = BraNSh(command_programms)
print(do_command_programms.log())

command_programms = Commands('exit', 'Выход')
do_command_programms = BraNSh(command_programms)
print(do_command_programms.log())

command_programms = Commands('help', 'Помощь')
do_command_programms = BraNSh(command_programms)
print(do_command_programms.log())

command_programms = Commands('exit', 'Выход')
do_command_programms = BraNSh(command_programms)
print(do_command_programms.log())

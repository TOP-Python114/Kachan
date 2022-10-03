from dataclasses import dataclass
import sys
import datetime
import time
from typing import Optional
from itertools import pairwise


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


class BraNSh():

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

        pass

    def log(self):

        """логирование и запись в файл"""

        self.__class__._count += 1
        if self.__class__._count < 51:
            file_name = 'log_command_f.txt'
            file = open(file_name, mode='a')
            log_data = f'{datetime.datetime.now()} {self.command} {self.args}'
            file.write(f'{log_data} \n')
            return log_data
        else:
            self.__class__._count = 1
            file_name = 'log_command_f.txt'
            file = open(file_name, mode='w')
            log_data = f'{datetime.datetime.now()} {self.command} {self.args}'
            file.write(f'{log_data} \n')
            return log_data

    def exit(self):

        """выход из программы"""

        self.todo = False
        print(self.command)
        sys.exit


command_programms = Commands('log','Запись')
do_command_programms = BraNSh(command_programms)
print(do_command_programms.log())

time.sleep(5)

command_programms = Commands('help','Помощь')
do_command_programms = BraNSh(command_programms)
print(do_command_programms.log())

command_programms = Commands('exit','Выход')
do_command_programms = BraNSh(command_programms)
print(do_command_programms.log())

command_programms = Commands('help','Помощь')
do_command_programms = BraNSh(command_programms)
print(do_command_programms.log())

command_programms = Commands('exit','Выход')
do_command_programms = BraNSh(command_programms)
print(do_command_programms.log())

"""Упражнение 67. Найти периметр многоугольника
Напишите программу для расчета периметра заданного многоугольника.
Начните с запроса у пользователя координат x и y первой точки многоугольника. Продолжайте запрашивать координаты следующих точек фигуры, пока пользователь не оставит строку ввода координаты по оси x пустой.
После ввода каждой пары значений вы должны вычислить длину очередной стороны многоугольника и прибавить полученное значение к будущему ответу.
По окончании ввода необходимо вычислить расстояние от последней введенной точки до первой, чтобы замкнуть фигуру, и вывести итоговый результат.
Для задачи №67 из Стивенсона реализуйте объектную модель из трёх классов: Polygon, LineSegment, Point.
Используйте композицию. Для расчёта значений используйте геттеры/сеттеры.
"""


@dataclass()
class Point:
    x: int
    y: int


@dataclass
class LineSegment:

    """Определяет длину отрезка"""

    point1: Point
    point2: Point

    @property
    def length_line(self) -> float:

        """Длина отрезка d2= (х2— х1)2+ (y2— y1)2"""

        return round(((self.point2.x - self.point1.x) ** 2 + (self.point2.y - self.point1.y) ** 2) ** 0.5,1)

class Polygon(list):

    """Определяет многоугольник"""

    def __init__(self: list[Point]):
        super().__init__()

    @property
    def perimeter(self):

        """Вычисляет периметр многоугольника при наличии трёх и более точек"""

        if len(self) < 3:
            raise ValueError('Задайте минимум три точки для построения многоугольника')

        else:
            return sum(
                LineSegment(p1, p2).length_line
                for p1, p2 in pairwise(self+[self[0]])
            )


point1 = Point(1, 2)
point2 = Point(1, 5)

line_seg = LineSegment(point1,point2)
print(line_seg.length_line)

pentagon = Polygon()

pentagon.append(Point(0, 0))
pentagon.append(Point(3, 4))
pentagon.append(Point(3, 0))
pentagon.append(Point(3, 7))
pentagon.append(Point(3, 18))

try:
    print(pentagon.perimeter)
except ValueError as e:
    print(e)

"""Для задачи №67 из Стивенсона реализуйте объектную модель из трёх классов: Polygon, LineSegment, Point. Используйте композицию. Для расчёта значений используйте геттеры/сеттеры. Начните с запроса у пользователя координат x и y первой точки многоугольника. Продолжайте запрашивать координаты следующих точек фигуры, пока пользователь не оставит строку ввода координаты по оси x пустой"""

from dataclasses import dataclass
from itertools import pairwise


@dataclass
class Point:
    """Описывает объект точки на плоскости в декартовой системе координат."""
    x: int
    y: int


@dataclass
class LineSegment:
    """Описывает объект отрезка, заданного двумя точками."""

    point1: Point
    point2: Point

    @property
    def length(self) -> float:
        """Возвращает округлённую до одного десятичного знака длину отрезка, как расстояние между двумя точками.

        d = √(х2 — х1)² + (y2 — y1)²⌝
        """
        dx = self.point2.x - self.point1.x
        dy = self.point2.y - self.point1.y
        return round((dx**2 + dy**2)**0.5, 1)


class Polygon(list):
    """Описывает многоугольник, заданный тремя и более точками."""

    def __init__(self):
        super().__init__()

    @property
    def perimeter(self) -> float:
        """Вычисляет и возвращает периметр многоугольника как сумму длин отрезков между попарно взятыми точками."""
        if len(self) < 3:
            raise ValueError('Задайте минимум три точки для построения многоугольника')
        else:
            return sum(
                LineSegment(p1, p2).length
                for p1, p2 in pairwise(self + [self[0]])
            )


point1 = Point(1, 2)
point2 = Point(1, 5)

line_seg = LineSegment(point1,point2)
print(line_seg.length)

pentagon = Polygon()

info = True
while info:
    x = input('Введите координату x: \n')
    if x == '':
        info = False
        print('Ввод точек окончен')
        break
    else:
        y = input('Введите координату y: \n')
        pentagon.append(Point(int(x), int(y)))
try:
    print(pentagon.perimeter)
except ValueError as e:
    print(e)

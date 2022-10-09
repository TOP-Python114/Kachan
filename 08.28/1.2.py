
#Упражнение 67. Найти периметр многоугольника
#Напишите программу для расчета периметра заданного многоугольника.
#Начните с запроса у пользователя координат x и y первой точки многоугольника. Продолжайте запрашивать координаты следующих точек фигуры, пока пользователь не оставит строку ввода координаты по оси x пустой.
#После ввода каждой пары значений вы должны вычислить длину очередной стороны многоугольника и прибавить полученное значение к будущему ответу.
#По окончании ввода необходимо вычислить расстояние от последней введенной точки до первой, чтобы замкнуть фигуру, и вывести итоговый результат.
#Для задачи №67 из Стивенсона реализуйте объектную модель из трёх классов: Polygon, LineSegment, Point.
#Используйте композицию. Для расчёта значений используйте геттеры/сеттеры.
from dataclasses import dataclass
from itertools import pairwise
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

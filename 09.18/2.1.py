# Напишите реализации нужных классов, так чтобы у вас получился Мост между назначением самолёта и сферой использования.

from abc import ABC, abstractmethod


# Passenger & Cargo Carriers пассажиры и грузы
class Carrier(ABC):
    @abstractmethod
    def carry_military(self, items):
        pass

    @abstractmethod
    def carry_commercial(self, items):
        pass


# ДОБАВИТЬ: документацию класса
class Cargo(Carrier):
    # ДОБАВИТЬ: документацию метода
    def carry_military(self, items):
        print("The plane carries", items, "military goods")

    # ДОБАВИТЬ: документацию метода
    def carry_commercial(self, items):
        print("The plane carries", items, "commercial goods")


# ДОБАВИТЬ: документацию класса
class Passenger(Carrier):
    # ДОБАВИТЬ: документацию метода
    def carry_military(self, passengers):
        print("The plane carries", passengers, "soldiers")

    # ДОБАВИТЬ: документацию метода
    def carry_commercial(self, passengers):
        print("The plane carries", passengers, "passengers")


# Military & Commercial Planes Военный и коммерческий
class Plane(ABC):
    @abstractmethod
    def display_description(self):
        pass

    @abstractmethod
    def add_objects(self, new_objects):
        pass


class Commercial(Plane):
    """Наследование от Plane и создание класса коммерческого самолета"""

    def __init__(self, carrier: Carrier, objects):
        self.carrier = carrier
        self.objects = objects

    # ДОБАВИТЬ: документацию метода
    def display_description(self):
        self.carrier.carry_commercial(self.objects)

    # ДОБАВИТЬ: документацию метода
    def add_objects(self, new_objects):
        self.objects += new_objects


class Military(Plane):
    """Наследование от Plane и создание класса военного самолета"""

    # ИСПРАВИТЬ: этот конструктор полностью повторяет таковой в родственном классе Commercial — во избежание дублирования кода стоит вынести метод в базовый класс
    def __init__(self, carrier: Carrier, objects):
        self.carrier = carrier
        self.objects = objects

    # ДОБАВИТЬ: документацию метода
    def display_description(self):
        self.carrier.carry_military(self.objects)

    # ДОБАВИТЬ: документацию метода
    # ИСПРАВИТЬ: аналогично — если нет разницы между методами в родственных классах, то имеет смысл заменить абстрактный метод на обычный и наследовать его
    def add_objects(self, new_objects):
        self.objects += new_objects


# КОММЕНТАРИЙ: прописывание документации и комментариев очень помогает систематизировать своё понимание кода, что особенно полезно во время обучения


cargo = Cargo()
passenger = Passenger()

military = Military(passenger, 100)
military.display_description()
military.add_objects(25)
military.display_description()

commercial = Commercial(cargo, 10)
commercial.display_description()
commercial.add_objects(350)
commercial.display_description()


# ДОБАВИТЬ: под меткой tests закомментированные результаты выполнения скрипта с различными входными данными
# tests:


# ИТОГ: очень хорошо — 5/6

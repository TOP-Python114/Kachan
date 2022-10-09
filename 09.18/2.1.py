
#Шаблон проектирования: Мост

#  ==========  1  ==========

#Напишите реализации нужных классов, так чтобы у вас получился Мост между назначением самолёта и сферой использования.

from abc import ABC, abstractmethod

# Passenger & Cargo Carriers пассажиры и грузы
class Carrier(ABC):
    @abstractmethod
    def carry_military(self, items):
        pass

    @abstractmethod
    def carry_commercial(self, items):
        pass


class Cargo(Carrier):
    def carry_military(self, items):
        print("The plane carries ", items, " military goods")

    def carry_commercial(self, items):
        print("The plane carries ", items, " commercial goods")


class Passenger(Carrier):
    def carry_military(self, passengers):
        print("The plane carries ", passengers, " soldiers")

    def carry_commercial(self, passengers):
        print("The plane carries ", passengers, " passengers")


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

    def __init__(self,  carrier: Carrier, objects):
        self.carrier = carrier
        self.objects = objects

    def display_description(self):
        self.carrier.carry_commercial(self.objects)

    def add_objects(self, new_objects):
        self.objects += new_objects

class Military(Plane):
    """Наследование от Plane и создание класса военного самолета"""

    def __init__(self, carrier: Carrier, objects):
        self.carrier = carrier
        self.objects = objects

    def display_description(self):
        self.carrier.carry_military(self.objects)

    def add_objects(self, new_objects):
        self.objects += new_objects


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



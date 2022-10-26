#Абстрактная фабрика может быть использована для выделения сущностей в разные семейства.
#Предположим, у нас есть объектная модель различных ресторанных блюд, которые наследуются от абстрактного класса Dish.
# Этот класс, например, может объявлять необходимость наличия у производных классов таких атрибутов как:
# название, описание, список ингридиентов, стоимость и метод потребления. Классы наследники, соответственно, реализуют эти требования.

#Dish(ABC)
#  └───────Dish1
#  └───────Dish2
#  └───────Dish3
#  └-------...
#Но помимо этих объединяющих атрибутов, блюда могут быть сгруппированы по кухням, например, блюда русской кухни и блюда азиатской кухни.

#Таким образом, мы можем составить цепочку фабрик,
#наследуемых от абстрактной фабрики. В этом примере, каждая фабрика может формировать набор блюд (закуска, первое и второе, например) для конкретной кухни.

#Factory(ABC)
#    └────────Factory1
#   └────────Factory2

#Реализуйте шаблон Абстрактной фабрики, который позволял бы создавать объекты либо одной, либо другой кухни — в зависимости от переданной в stdin строки.

#Фабрики исполнители пусть отвечают только за подачу блюд — т.е. необходимо создать экземпляр блюда и объявить в stdout, что такое-то блюдо подано.

from abc import ABC, abstractmethod
from enum import Enum
from inspect import getmembers, isclass, isabstract
from sys import modules

class Dish(ABC):
    FOOD = True
    @abstractmethod
    def ingredients_dish(self):
        """Формирует состав блюда"""
        pass

    def serve_dish(self):
        """Формирует блюдо"""
        pass

    def price_dish(self):
        """Рассчитывает цену"""
        pass



class Sushi(Dish):
    def __init__(self, portion:int):
        """
        :param portion: порция
        """
        self.portion = portion

    def ingredients_dish(self):
        print(f'Ингридиенты: \nикра летучей рыбы\nрис\nлосось')

    def serve_dish(self):
        print('Суши готовы')

    def price_dish(self):
        price = self.portion*550
        print(f'Количество порций: {self.portion}\nЦена: {price} руб.')


class Borsch(Dish):
    def __init__(self, portion:int):
        self.portion = portion

    def ingredients_dish(self):
        print(f'Ингридиенты: \nСвекла\nМорковь\nКартофель\nЗелень\nСвинина')

    def serve_dish(self):
        print('Борщ готов')

    def price_dish(self):
        price = self.portion * 200
        print(f'Количество порций: {self.portion}\nЦена: {price} руб.')


class WOK(Dish):
    def __init__(self, portion: int):
        self.portion = portion

    def ingredients_dish(self):
        print(f'Ингридиенты: \nЛапша\nМорковь\nКурица\nПерец\nСоус Терияки')

    def serve_dish(self):
        print('WOK готов')

    def price_dish(self):
        price = self.portion * 280
        print(f'Количество порций: {self.portion}\nЦена: {price} руб.')

class Pancakes(Dish):
    def __init__(self, portion: int):
        self.portion = portion

    def ingredients_dish(self):
        print(f'Ингридиенты: \nМолоко\nМука\nЯйца\nСахар\nСоль\nДжем')

    def serve_dish(self):
        print('Блины готовы')

    def price_dish(self):
        price = self.portion * 280
        print(f'Количество порций: {self.portion}\nЦена: {price} руб.')


class Fish_which_potatoes(Dish):
    def __init__(self, portion: int):
        self.portion = portion

    def ingredients_dish(self):
        print(f'Ингридиенты: \nРыба\nКартофель\nЯйца\nСпеции\nСоль')

    def serve_dish(self):
        print('Рыба с картошкой готова')

    def price_dish(self):
        price = self.portion * 450
        print(f'Количество порций: {self.portion}\nЦена: {price} руб.')


class lasagna(Dish):
    def __init__(self, portion: int):
        self.portion = portion

    def ingredients_dish(self):
        print(f'Ингридиенты: \nМука\nКурица\nТоматы\nСпеции\nСоль')

    def serve_dish(self):
        print('Лазанья готова')

    def price_dish(self):
        price = self.portion * 250
        print(f'Количество порций: {self.portion}\nЦена: {price} руб.')


class Pasta(Dish):
    def __init__(self, portion: int):
        self.portion = portion

    def ingredients_dish(self):
        print(f'Ингридиенты: \nЛапша\nКурица\nТоматы\nСпеции\nСоль')

    def serve_dish(self):
        print('Паста готова')

    def price_dish(self):
        price = self.portion * 300
        print(f'Количество порций: {self.portion}\nЦена: {price} руб.')


class Pizza(Dish):
    def __init__(self, portion: int):
        self.portion = portion

    def ingredients_dish(self):
        print(f'Ингридиенты: \nМука\nКурица\nТоматы\nСпеции\nСоль\nГрибы')

    def serve_dish(self):
        print('Пицца готова')

    def price_dish(self):
        price = self.portion * 600
        print(f'Количество порций: {self.portion}\nЦена: {price} руб.')


class Chop_with_vegetables(Dish):
    def __init__(self, portion: int):
        self.portion = portion

    def ingredients_dish(self):
        print(f'Ингридиенты: \nТоматы\nСвинина\nПерец\nСпеции\nСоль\nГрибы')

    def serve_dish(self):
        print('Отбивная с овощами готова')

    def price_dish(self):
        price = self.portion * 600
        print(f'Количество порций: {self.portion}\nЦена: {price} руб.')


class Pork_ribs_with_cheese(Dish):
    def __init__(self, portion: int):
        self.portion = portion

    def ingredients_dish(self):
        print(f'Ингридиенты: \nСыр\nСвинина\nЯйцо\nСпеции\nСоль\nГрибы')

    def serve_dish(self):
        print('Ребрышки с сыром готовы')

    def price_dish(self):
        price = self.portion * 600
        print(f'Количество порций: {self.portion}\nЦена: {price} руб.')


class DishesFactory(ABC):
    FACTORY = True
    @staticmethod
    @abstractmethod
    def create_dish(portion: int):
        """Генерирует объект для формирования блюда"""
        pass


class Italian_factory(DishesFactory):
    @staticmethod
    def create_dish(portion: int, idx: int):
        if idx == 5:
            return Pasta(portion)
        elif idx == 6:
            return Pizza(portion)
        elif idx == 10:
            return lasagna(portion)
        else:
            raise ValueError(f'Требуется уточнение меню')


class Japan_factory(DishesFactory):
    @staticmethod
    def create_dish(portion: int, idx: int):
        if idx == 8:
            return Sushi(portion)
        elif idx == 9:
            return WOK(portion)
        else:
            raise ValueError(f'Требуется уточнение меню')


class European_factory(DishesFactory):
    @staticmethod
    def create_dish(portion: int, idx: int):
        if idx == 2:
            return Chop_with_vegetables(portion)
        elif idx == 3:
            return Fish_which_potatoes(portion)
        else:
            raise ValueError(f'Требуется уточнение меню')


class Russian_factory(DishesFactory):
    @staticmethod
    def create_dish(portion: int, idx: int):
        if idx == 1:
            return Borsch(portion)
        elif idx == 4:
            return Pancakes(portion)
        elif idx == 7:
            return Pork_ribs_with_cheese(portion)
        else:
            raise ValueError(f'Требуется уточнение меню')


class HotDishCreate:
    """Собирает информации о генерируемом объекте и возврат объекта."""
    AvailableDishes = Enum(
        'AvailableDishes',
        [
            pair[0]
            for pair in getmembers(
                modules[__name__],
                lambda obj: isclass(obj)
                            and getattr(obj, 'FOOD', False)
                            and not isabstract(obj)
            )
        ]
    )
    AvailableKichen = Enum(
        'AvailableKichen',
        [
            pair[0]
            for pair in getmembers(
            modules[__name__],
            lambda obj: isclass(obj)
                        and getattr(obj, 'FACTORY', False)
                        and not isabstract(obj)
        )
        ]
    )
    factories = {}
    initialized = False

    def __init__(self):
        if not self.initialized:
            self.initialized = True
            for dish in self.AvailableKichen:
                self.factories[dish] = eval(dish.name)()

    def print_food(self) -> None:
        """Отображает доступные блюда."""
        print('Блюда:')
        for dish in self.AvailableDishes:
            print(f"{dish.value}. {dish.name}")

    def choose_dishes(self) -> int:
        """Запрашивает блюдо у пользователя"""
        lf = len(self.AvailableDishes)
        return int(input(f' > выберите блюдо (1–{lf}): '))

    def choose_portion(self) -> int:
        """Определяет количество порций"""
        return int(input(' > укажите количество порций: '))

    def make_food(self) -> Dish:
        """Формирует заказ блюда"""
        self.print_food()
        idx = self.choose_dishes()
        portion = self.choose_portion()
        if idx in (2, 3):
            return self.factories[self.AvailableKichen(1)].create_dish(portion, idx)
        elif idx in (5, 6, 10):
            return self.factories[self.AvailableKichen(2)].create_dish(portion, idx)
        elif idx in (8, 9):
            return self.factories[self.AvailableKichen(3)].create_dish(portion, idx)
        elif idx in (1, 4, 7):
            return self.factories[self.AvailableKichen(4)].create_dish(portion, idx)
        else:
            raise ValueError(f'Вы не выбрали не одного блюда')


order = HotDishCreate()
dish = order.make_food()
dish.ingredients_dish()
dish.serve_dish()
dish.price_dish()
#stdout
# Блюда:
# 1. Borsch
# 2. Chop_with_vegetables
# 3. Fish_which_potatoes
# 4. Pancakes
# 5. Pasta
# 6. Pizza
# 7. Pork_ribs_with_cheese
# 8. Sushi
# 9. WOK
# 10. lasagna
#  > выберите блюдо (1–10): 8
#  > укажите количество порций: 1
# Ингридиенты:
# икра летучей рыбы
# рис
# лосось
# Суши готовы
# Количество порций: 1
# Цена: 550 руб.
#########################
# Блюда:
# 1. Borsch
# 2. Chop_with_vegetables
# 3. Fish_which_potatoes
# 4. Pancakes
# 5. Pasta
# 6. Pizza
# 7. Pork_ribs_with_cheese
# 8. Sushi
# 9. WOK
# 10. lasagna
#  > выберите блюдо (1–10): 10
#  > укажите количество порций: 1
# Ингридиенты:
# Мука
# Курица
# Томаты
# Специи
# Соль
# Лазанья готова
# Количество порций: 1
# Цена: 250 руб.

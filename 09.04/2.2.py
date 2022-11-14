# Абстрактная фабрика может быть использована для выделения сущностей в разные семейства.
# Предположим, у нас есть объектная модель различных ресторанных блюд, которые наследуются от абстрактного класса Dish.
# Этот класс, например, может объявлять необходимость наличия у производных классов таких атрибутов как:
# название, описание, список ингридиентов, стоимость и метод потребления. Классы наследники, соответственно, реализуют эти требования.
#
# Dish(ABC)
#  └───────Dish1
#  └───────Dish2
#  └───────Dish3
#  └-------...
# Но помимо этих объединяющих атрибутов, блюда могут быть сгруппированы по кухням, например, блюда русской кухни и блюда азиатской кухни.
#
# Таким образом, мы можем составить цепочку фабрик,
# наследуемых от абстрактной фабрики. В этом примере, каждая фабрика может формировать набор блюд (закуска, первое и второе, например) для конкретной кухни.
#
# Factory(ABC)
#    └────────Factory1
#   └────────Factory2
#
# Реализуйте шаблон Абстрактной фабрики, который позволял бы создавать объекты либо одной, либо другой кухни — в зависимости от переданной в stdin строки.
#
# Фабрики исполнители пусть отвечают только за подачу блюд — т.е. необходимо создать экземпляр блюда и объявить в stdout, что такое-то блюдо подано.

from abc import ABC, abstractmethod
from enum import Enum
from inspect import getmembers, isclass, isabstract
from sys import modules
from typing import Any, Type


class Dish(ABC):
    FOOD = True

    @abstractmethod
    def ingredients_dish(self):
        """Формирует состав блюда"""

    # ОТВЕТИТЬ: почему эти два метода в отличие от первого не стали делать абстрактными?
    def serve_dish(self):
        """Формирует блюдо"""

    def price_dish(self):
        """Рассчитывает цену"""


class Sushi(Dish):
    def __init__(self, portion: int):
        """
        :param portion: количество порций
        """
        self.portion = portion

    def ingredients_dish(self):
        print(f'Ингридиенты: \nИкра летучей рыбы\nРис\nЛосось')

    # КОММЕНТАРИЙ: если немного порассуждать и вспомнить SRP (принцип единственной ответственности), то за сервировку блюда отвечает скорее ресторан или официант, если у нас есть такая сущность, — но едва ли блюдо само себя сервирует =) это не является чем-то обязательным и должно определяться контекстом проекта, но полагаю, что вам будет полезно обратить внимание на этот аспект
    def serve_dish(self):
        print('Суши готовы')

    def price_dish(self):
        price = self.portion * 550
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
    # ИСПРАВИТЬ: у вас есть базовый класс и есть без изменений повторяющийся в подклассах метод — это прям очень явный сигнал, что этот метод следовало прописать в базовом классе — не абстрактным, а обычным методом
    def __init__(self, portion: int):
        self.portion = portion

    def ingredients_dish(self):
        print(f'Ингридиенты: \nЛапша\nМорковь\nКурица\nПерец\nСоус Терияки')

    def serve_dish(self):
        print('WOK готов')

    # ИСПРАВИТЬ: аналогично — в этом методе от класса к классу меняется только одно значение, почему бы не убрать его в параметр и не перенести метод в базовый класс?
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


class Lasagna(Dish):
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
    # ИСПРАВИТЬ: сигнатуры методов реализаций должны соответствовать сигнатуре соответствующего абстрактного метода — если все методы реализации должны использовать параметр idx, то необходимо указать его в сигнатуре абстрактного метода
    def create_dish(portion: int):
        """Генерирует объект для формирования блюда"""


class Italian_factory(DishesFactory):
    @staticmethod
    def create_dish(portion: int, idx: int):
        # ИСПРАВИТЬ: в условии задачи предполагалось, что фабрика сгенерирует набор соответствующих блюд, а не одно на выбор — но если решили делать так, то лучше здесь вычислить перечислитель аналогично AvailableDishes, но только из итальянских блюд — а потом в этот метод передавать имя того блюда (класса), которое хотите получить (см. пример ниже)
        if idx == 5:
            return Pasta(portion)
        # КОММЕНТАРИЙ: а эти индексы совсем не статичны, они могут измениться даже при изменении всего лишь порядка расположения классов в коде — а значит при любом масштабировании модели вам придётся их вручную выискивать и переписывать — это грустная история, поверьте
        elif idx == 6:
            return Pizza(portion)
        elif idx == 10:
            return Lasagna(portion)
        # КОММЕНТАРИЙ: не говоря уже о том, что при увеличении количества блюд одной кухни, вам придётся дописывать сюда очередные elif — а это прямое нарушение OCP (принципа открытости/закрытости)
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
    # ИСПРАВИТЬ: если мы формируем список всех блюд, независимо от кухни, то потом нам приходится как-то распределять их по кухням — что вы и делаете в методе make_food() — раз у нас есть фабрики отдельных кухонь, то лучше сразу сопоставить конкретной фабрике те классы, с которыми она может работать
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
    # ИСПРАВИТЬ: повторяющийся код выносится в функции или методы
    AvailableKitchens = Enum(
        'AvailableKitchens',
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
            for dish in self.AvailableKitchens:
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
        # ИСПРАВИТЬ: и с этими индексами вы тоже будете страдать, когда придёт время масштабировать модель классов
        if idx in (2, 3):
            return self.factories[self.AvailableKitchens(1)].create_dish(portion, idx)
        elif idx in (5, 6, 10):
            return self.factories[self.AvailableKitchens(2)].create_dish(portion, idx)
        elif idx in (8, 9):
            return self.factories[self.AvailableKitchens(3)].create_dish(portion, idx)
        elif idx in (1, 4, 7):
            return self.factories[self.AvailableKitchens(4)].create_dish(portion, idx)
        else:
            raise ValueError(f'Вы не выбрали не одного блюда')


# order = HotDishCreate()
# dish = order.make_food()
# dish.ingredients_dish()
# dish.serve_dish()
# dish.price_dish()


# stdout
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


# ИТОГ: вижу, что поработали вы довольно много и в целом хорошо, а значит тем важнее теперь осмыслить комментарии и выполнить работу над ошибками — 7/10


# ИСПОЛЬЗОВАТЬ: пример альтернативной организации модели

def get_classes_names(enum_name: str, *attributes: str, module_name: str = __name__) -> Type[Enum]:
    """Возвращает перечислитель из имён классов определённого модуля, содержащих определённый атрибут. Абстрактные классы игнорируются.

    :param enum_name: имя класса перечислителя
    :param attributes: имена атрибутов, которые должны присутствовать у класса
    :param module_name: имя модуля, в котором необходимо проводить инспекцию
    :return: объект класса перечислителя
    """
    return Enum(
        enum_name,
        [
            name
            for name, class_obj in getmembers(
                modules[module_name],
                lambda obj: isclass(obj)
                            # КОММЕНТАРИЙ: раз уж вынес этот код в отдельную функцию, то решил сделать его чуть более универсальным — авось пригодится =)
                            and all(map(
                                lambda attr: getattr(obj, attr, False),
                                attributes
                            ))
                            and not isabstract(obj)
            )
        ]
    )


class CheBaBa(Dish):
    # КОММЕНТАРИЙ: атрибут класса, определяющий принадлежность к определённой кухне
    VIE = True

    def ingredients_dish(self):
        pass

class BunCha(Dish):
    VIE = True

    def ingredients_dish(self):
        pass


class VietnamFactory(DishesFactory):
    # КОММЕНТАРИЙ: вот здесь формируется перечислитель блюд только вьетнамской кухни
    Dishes = get_classes_names('Dishes', 'VIE')

    @staticmethod
    def create_dish(dish: Dishes, portions: int) -> Dish:
        """
        :param dish: название блюда вьетнамской кухни – экземпляр перечислителя VietnamFactory.Dishes
        :param portions: количество порций
        :return: экземпляр блюда вьетнамской кухни
        """
        try:
            return eval(dish.name)()
        except AttributeError:
            raise ValueError(f'Требуется уточнение меню')


# КОММЕНТАРИЙ: класс наследует от HotDishCreate конструктор, создание фабрик и те методы, которые не переопределены — это для экономии времени, а не пример для подражания =)
class Restaurant(HotDishCreate):
    AvailableKitchens = get_classes_names('AvailableKitchens', 'FACTORY')

    def print_kitchens(self):
        """Отображает доступные кухни."""
        print('Кухни:')
        for kitchen in self.AvailableKitchens:
            print(f"{kitchen.value}. {kitchen.name}")

    def choose_kitchen(self, ):
        """Запрашивает кухню у пользователя"""
        lf = len(self.AvailableKitchens)
        return int(input(f' > выберите кухню (1–{lf}): '))

    def print_food(self, kitchen: Type[Enum]) -> None:
        """Отображает доступные блюда конкретной кухни."""
        print('Блюда:')
        for dish in kitchen:
            print(f"{dish.value}. {dish.name}")

    def make_food(self) -> Dish:
        # КОММЕНТАРИЙ: раз теперь блюда у нас "привязаны" к кухням, то имеет смысл предложить пользователю выбрать сначала кухню — аналог подачи разных меню для каждой кухни в одном ресторане
        self.print_kitchens()
        # название кухни — экземпляр перечислителя
        kitchen = self.AvailableKitchens(self.choose_kitchen())
        # объект кухни — объект класса фабрики
        Factory = eval(kitchen.name)

        self.print_food(Factory.Dishes)
        # название блюда — экземпляр перечислителя
        dish = Factory.Dishes(self.choose_dishes())

        cnt = self.choose_portion()
        try:
            return self.factories[kitchen].create_dish(dish, cnt)
        except:
            raise ValueError('')


r = Restaurant()
# КОММЕНТАРИЙ: этот тест работает только с пунктом 5. VietnamFactory — потому что только в этом классе сформирован перечислитель блюд конкретной кухни
d = r.make_food()
print(d)

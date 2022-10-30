class ClassBuilder:
    def __init__(self, name):
        self.name = name
        # ИСПРАВИТЬ: этот список вы используете как словарь — так и сделайте его словарём
        self.elements: list[str] = []

    # ИСПРАВИТЬ: а в тестах в value передаёте число — так какие типы возможны для value?
    def add_field(self, attrib: str = '', value: str = ''):
        """
        Добавляет свойства объекта

        :param attrib: свойство объекта
        :param value: значение свойства объекта
        """
        # ИСПРАВИТЬ: и новые элементы в словарь добавлять удобнее с помощью словарных методов
        names = [x for x, y in self.elements]
        if attrib not in names:
            self.elements += [(attrib, value)]
        return self

    def __str__(self):
        # ИСПРАВИТЬ: в пустом классе не должно быть заголовка конструктора (см. тест ниже vs. пример в условии)
        result = f'class {self.name.capitalize()}:\n\tdef __init__(self):\n'
        if self.elements:
            for attrib, value in self.elements:
                # ИСПОЛЬЗОВАТЬ: машиночитаемое строковое представление __repr__() str объекта возвращает строку, содержащую кавычки — что в данном случае необходимо
                result += f'\t\tself.{attrib} = {value!r}\n'
        else:
            result += f'\n\tpass'
        return result


class_data = ClassBuilder('Person')\
    .add_field('name', '')\
    .add_field('age', 20)\
    .add_field('fio', 'Иванова')
print(class_data)

class_data1 = ClassBuilder('Person1')\
    .add_field('name', 'Полина')\
    .add_field('age', 10)\
    .add_field('fio', 'Смирнова')\
    .add_field('hobby', 'swimming')
print(class_data1)

class_data2 = ClassBuilder('Foobar')
print(class_data2)


# stdout:
# class Person:
# 	def __init__(self):
# 		self.name = ""
# 		self.age = 20
        # КОММЕНТАРИЙ: без кавычек интерпретатор будет уверен, что Иванова — это переменная (unicode имена переменных тоже возможны)
# 		self.fio = Иванова

# class Person1:
# 	def __init__(self):
# 		self.name = Полина
# 		self.age = 10
# 		self.fio = Смирнова
# 		self.hobby = swimming

# class Foobar:
# 	def __init__(self):
#
# 	pass


# ИТОГ: необходимо проработать указанные моменты, но в целом хорошо — 6/8

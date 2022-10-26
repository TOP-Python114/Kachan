
class ClassBuilder:
    def __init__(self, name):
        self.name = name
        self.elements: list[str] = []

    def add_field(self, attrib: str = '', value: str = ''):

        """Добавляет свойства объекта
        :param attrib: свойство объекта
        :param value: значение свойства объекта
        """

        names = [x for x, y in self.elements]
        if attrib not in names:
            self.elements += [(attrib, value)]
        return self

    def __str__(self):
        result = f'class {self.name.capitalize()}:\n\tdef __init__(self):\n'
        if self.elements:
            for attrib, value in self.elements:
                result += f'\t\tself.{attrib} = {value}\n'
        else:
            result += f'\n\t pass'
        return result


class_data = ClassBuilder('Person').add_field('name', '""').add_field('age', 20).add_field('fio', 'Иванова')
print(class_data)
class_data1 = ClassBuilder('Person1').add_field('name', 'Полина').add_field('age', 10).add_field('fio', 'Смирнова').add_field('hobby', 'swimming')
print(class_data1)
# stdout:
# class Person:
# 	def __init__(self):
# 		self.name = ""
# 		self.age = 20
# 		self.fio = Иванова
# class Person1:
# 	def __init__(self):
# 		self.name = Полина
# 		self.age = 10
# 		self.fio = Смирнова
# 		self.hobby = swimming

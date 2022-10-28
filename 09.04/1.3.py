class HTMLElement:
    """
    Формирует строку с HTML тегом
    """
    default_indent_size = 4

    def __init__(self, name: str, value: str = "", **kwargs: str):
        self.name = name
        self.value = value
        self.elements: list['HTMLElement'] = []
        self.kwargs = "".join([f' {i} = "{j}"' for i, j in kwargs.items()])

    def __str__(self):
        return self.__str()

    def __str(self, indent_lvl: int = 0):
        """
        Формирует строку вывода тэгов HTML

        :param indent_lvl: счетчик, используемый для расчета отступов строки
        """
        indent = ' ' * indent_lvl * self.__class__.default_indent_size
        ret = f'{indent}<{self.name}{self.kwargs}>{self.value}'
        if self.elements:
            for element in self.elements:
                ret += '\n' + element.__str(indent_lvl + 1)
            ret += f'\n{indent}</{self.name}>'
        else:
            ret += f'</{self.name}>'
        return ret


class HTMLBuilder:
    """
    """
    def __init__(self, root: str | HTMLElement, **kwargs: str):
        if isinstance(root, str):
            self.__root = HTMLElement(root, **kwargs)
        elif isinstance(root, HTMLElement):
            self.__root = root

    def add_child(self, name: str, value: str = "", **kwargs):
        """
        Добавляет новые тэги HTML

        :param name: наименование тэга
        :param value: значение тэга
        :param kwargs: дополнительные элементы тэга
        """
        self.__root.elements += [
            el := HTMLElement(name, value, **kwargs)
        ]
        return HTMLBuilder(el)

    def add_sibling(self, name: str, value: str = "", **kwargs: str):
        """
        Добавляет новые тэги HTML внутри предыдущего тега

        :param name: наименование тэга
        :param value: значение тэга
        :param kwargs: дополнительные элементы тэга
        """
        self.__root.elements += [
            HTMLElement(name, value, **kwargs)
        ]
        return self

    def __str__(self):
        return str(self.__root)

    def to_html(self):
        """Записывает данные в HTML файл"""
        with open('file.html', "w", encoding="utf-8") as fp:
            fp.write(str(self))
        return self


# noinspection PyAttributeOutsideInit
class CVBuilder:
    """
    Добавляет элементы и собирает данные в единую структуру
    """
    contacts = {}
    projects = {}

    def __init__(self,
                 fio: str,
                 age: int,
                 pos_name: str,
                 mail: str
                 ):
        self.fio = fio
        self.age = age
        self.pos_name = pos_name
        self.mail = mail

    def add_education(self, university, profession, year_end):
        """
        Добавляет информацию об университете, профессии и годе окончания

        :param university: университет
        :param profession: профессия
        :param year_end: год окончания
        :return: self
        """
        self.university = university
        self.profession = profession
        self.year_end = year_end
        return self

    def add_project(self, project, *image):
        """
        Добавляет данные о проекте

        :param project: проект
        :param image: ярлык проекта
        :return:
        """
        self.projects.update({project: image})
        return self

    def add_contact(self, **contacts):
        """
        Добавляет данные о контактах

        :param contacts: контакты
        """
        self.contacts.update(contacts)
        return self

    def build(self):
        html = HTMLBuilder('html')
        head = html.add_child('head').add_child('title', f'{self.fio}: портфолио')
        menu = html.add_child('body').add_child('div')
        info = menu.add_sibling('h2', 'Обо мне')
        if self.university:
            info.add_sibling("h3", f'Образование:')
            info.add_sibling("p", f'{self.university}, {self.profession}, {self.year_end}')
        if self.contacts:
            info.add_sibling("h3", f'Контакты:')
            for type_contact, contact in self.contacts.items():
                info.add_sibling("p", f'{type_contact}: {contact}')
        if self.projects:
            info.add_sibling("h3", f'Проекты:')
            for project, image in self.projects.items():
                info.add_sibling("p", f'{project}: {image}')
        return html


person1 = CVBuilder('Иванов Иван Иванович', 26, 'художник-фрилансер', 'ivv@abc.de')\
    .add_education('Архитектурная Академия', 'Компьютерный дизайн', 2019)\
    .add_project('Разработка логотипа для компании по производству снеков',
                 'https://education.ru/1456')\
    .add_contact(devianart='ivovuvan_in_art')\
    .add_contact(telegram='@ivovuvan')\
    .add_project('UI разработка для интернет-магазина для восковых дел мастеров',
                 'https://education.ru/gghgj',
                 'https://education.ru/gghgj54546')\
    .build().to_html()
print(person1)


# stdout:
# <html>
#     <head>
#         <title>Иванов Иван Иванович: портфолио</title>
#     </head>
#     <body>
#         <div>
#             <h2>Обо мне</h2>
#             <h3>Образование:</h3>
#             <p>Архитектурная Академия, Компьютерный дизайн, 2019</p>
#             <h3>Контакты:</h3>
#             <p>devianart: ivovuvan_in_art</p>
#             <p>telegram: @ivovuvan</p>
#             <h3>Проекты:</h3>
#             <p>Разработка логотипа для компании по производству снеков: ('https://education.ru/1456',)</p>
#             <p>UI разработка для интернет-магазина для восковых дел мастеров: ('https://education.ru/gghgj', 'https://education.ru/gghgj54546')</p>
#         </div>
#     </body>
# </html>

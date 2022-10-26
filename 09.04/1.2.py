
class HTMLElement:

    """Формирует строку с HTML тегом"""

    default_indent_size = 4

    def __init__(self, name: str, value: str = "", **kwargs: str):
        self.name = name
        self.value = value
        self.elements: list['HTMLElement'] = []
        self.kwargs = "".join([f' {i} = "{j}"' for i, j in kwargs.items()])

    def __str__(self):
        return self.__str()

    def __str(self, indent_lvl: int = 0):

        """Формирует строку вывода тэгов HTML
        :param indent_lvl: счетчик, используемый для расчета отступов строки
        """

        indent = ' ' * indent_lvl * self.__class__.default_indent_size
        ret = f'{indent}<{self.name}{self.kwargs}>{self.value}'
        if self.elements:
            for element in self.elements:
                ret += '\n' + element.__str(indent_lvl+1)
            ret += f'\n{indent}</{self.name}>'
        else:
            ret += f'</{self.name}>'
        return ret


class HTMLBuilder:

    def __init__(self, root: str | HTMLElement, **kwargs: str):
        if isinstance(root, str):
            self.__root = HTMLElement(root, **kwargs)
        elif isinstance(root, HTMLElement):
            self.__root = root

    def add_child(self, name: str, value: str = "", **kwargs):

        """Добавляет новые тэги HTML
        :param name: наименование тэга
        :param value: значение тэга
        :param **kwargs: дополнительные элементы тэга
        """

        self.__root.elements += [
            el := HTMLElement(name, value, **kwargs)
        ]
        return HTMLBuilder(el)

    def add_sibling(self, name: str, value: str = "", **kwargs: str):

        """Добавляет новые тэги HTML внутри предыдущего тега
        :param name: наименование тэга
        :param value: значение тэга
        :param **kwargs: дополнительные элементы тэга
        """

        self.__root.elements += [
            HTMLElement(name, value, **kwargs)
        ]
        return self

    def __str__(self):
        return str(self.__root)


body = HTMLBuilder('body', style = 'background-color:#f5bbe1')
menu = body.add_child('div', style='color:blueviolet').add_child('ul')
menu.add_child('li', 'File').add_child('p', 'New')\
.add_sibling('p', 'Open')\
.add_sibling('p', 'Save', style = 'font-size:18px')
menu.add_child('li', 'Edit')\
    .add_sibling('p', 'Undo')\
    .add_sibling('p', 'Redo')\
    .add_sibling('p', 'Cut')\
    .add_sibling('p', 'Copy')\
    .add_sibling('p', '')
print(body)

# stdout:
# <body style = "background-color:#f5bbe1">
#     <div style = "color:blueviolet">
#         <ul>
#             <li>File
#                 <p>New
#                     <p>Open</p>
#                     <p style = "font-size:18px">Save</p>
#                 </p>
#             </li>
#             <li>Edit
#                 <p>Undo</p>
#                 <p>Redo</p>
#                 <p>Cut</p>
#                 <p>Copy</p>
#                 <p></p>
#             </li>
#         </ul>
#     </div>
# </body>

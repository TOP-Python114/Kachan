from random import randrange as rr, choice as ch
from string import ascii_lowercase as alc


class TestCase:
    def __init__(self):
        self.messages = [
            ''.join(ch(alc) for _ in range(rr(3, 6)))
            for _ in range(1000)
        ]
        self.numbers = [
            (rr(10, 100) for _ in range(rr(4, 7)))
            for _ in range(1000)
        ]
        self.list = []
        self.msg: str = ''
        self.nums: int = 0

    def print_msg(self):
        """Генерирует строковый элемент"""
        self.msg = self.messages.pop()
        self.list.append(self.msg)
        print(self.msg)
        return self.list

    def sum_nums(self):
        """Генерирует числовой элемент"""
        nums = self.numbers.pop()
        self.number = sum(nums)
        self.list.append(self.number)
        print(self.number)
        return self.list

    def history(self):
        """Показывает текущий набор элементов"""
        print(self.list)

    def undo(self):
        """Удаляет последний элемент"""
        self.last = self.list.pop()
        return self.list

    def redo(self):
        """Отменяет удаление последнего элемента"""
        self.list.append(self.last)
        return self.list


class Command:
    """
    Базовый класс
    """
    def execute(self):
        raise NotImplementedError()


class CommandBase(Command):
    """
    Класс, принимающий объект TestCase
    """
    def __init__(self, element):
        self.element = element


class AdditionMsg(CommandBase):
    def execute(self):
        """Вызывает метод, формирующий строковый элемент"""
        self.element.print_msg()


class AdditionNum(CommandBase):
    def execute(self):
        """Вызывает метод, формирующий числовой элемент"""
        self.element.sum_nums()


class RedoCommand(CommandBase):
    def execute(self):
        """Вызывает метод, осуществляющий повторное выполнение отмененной операции"""
        self.element.redo()


class UndoCommand(CommandBase):
    def execute(self):
        """Вызывает метод, отменяющий последнюю операцию"""
        self.element.undo()


class HistoryCommand(CommandBase):
    def execute(self):
        """Вызывает метод, для отображения текущих элементов"""
        self.element.history()


class AllCommands:
    """
    Класс формирует пул из команд
    """
    def __init__(self, addmsg, addnum, undo, redo, history):
        self.addmsg = addmsg
        self.addnum = addnum
        self.undo = undo
        self.redo = redo
        self.history = history

    def add_msg(self):
        """Вызывает метод, формирующий строковый элемент"""
        self.addmsg.execute()

    def add_num(self):
        """Вызывает метод, формирующий числовой элемент"""
        self.addnum.execute()

    def redo_com(self):
        """Вызывает метод, осуществляющий повторное выполнение отмененной операции"""
        self.redo.execute()

    def undo_com(self):
        """Вызывает метод, отменяющий последнюю операцию"""
        self.undo.execute()

    def history_com(self):
        """Вызывает метод, для отображения текущих элементов"""
        self.history.execute()


test = TestCase()
commands = AllCommands(
    addmsg=AdditionMsg(test),
    addnum=AdditionNum(test),
    undo=UndoCommand(test),
    redo=RedoCommand(test),
    history=HistoryCommand(test)
)

commands.add_msg()
commands.add_msg()
commands.add_num()
commands.history_com()
commands.undo_com()
commands.history_com()
commands.undo_com()
commands.history_com()
commands.redo_com()
commands.history_com()
commands.add_msg()
commands.add_num()
commands.history_com()

# syq
# nooay
# 266
# ['syq', 'nooay', 266]
# ['syq', 'nooay']
# ['syq']
# ['syq', 'nooay']
# wxh
# 217
# ['syq', 'nooay', 'wxh', 217]

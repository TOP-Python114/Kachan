#Создайте высокоуровневую реализацию оболочки командного интерпретатора.
#Класс BraNSh(Brand New Shell)
#Экземпляр класса создаётся при старте приложения, после чего запускается обработка команд.
#Команды с аргументами получаем из stdin.
# Каждая команда должнаn быть представлена как объект класса Command.
# Далее, команда выполняется, а её вывод отправляется в stdout.
# Если журналирование включено, то текст команды с аргументами и текст её вывода пишется в файл - журнал.
# Реализуйте возможность хранения заданного количества(50 по умолчанию) последних введёных команд
#и поиска по подстроке среди этих команд.
# При вводе команды exit обработка команд останавливается.
# Атрибуты экземпляра:
#- журналирование команд и их вывода: bool
# Методы:
#- запуск обработки команд -> ?
#- обработка команд -> ?
#- остановка обработки команд -> ?
# Остальные атрибуты и методы продумайте самостоятельно.
# Класс Command
#Вывод команд для простоты реализуйте в виде словаря: {'command1': 'output of command1', ...}
# Атрибуты экземпляра:
#- команда: str
#- аргументы команды: str
# Методы:
#- выполнение команды -> str
# Остальные атрибуты и методы продумайте самостоятельно.

from typing import Optional
from datetime import datetime as dt
from sys import exit
from time import sleep


class Command:
    """Объект команды хранит в атрибутах имя и аргументы команды, позволяет выполнять команду и возвращать строку с результатом выполнения команды."""

    # КОММЕНТАРИЙ: этот класс предназначен для одной команды

    def __init__(self, command: str, args: str):
        self.command = command
        self.args = args
        # УДАЛИТЬ: в описанной в условии модели объект команды не должен хранить информацию о других командах
        self.history = {}

    # ИСПРАВИТЬ: здесь резонно выводить информацию о самой команде, а не о словаре
    def __str__(self):
        """Выводит словарь, содержащий команды."""
        return self.history

    # УДАЛИТЬ: метод не отвечает требуемой объектной модели
    def add(self) -> dict[str, str]:
        """Добавляет команду в словарь."""
        self.history[self.command] = self.args
        return self.history

    def execute(self) -> str:
        """Возвращает результат выполнения команды."""
        # КОММЕНТАРИЙ: хорошо, результат выполнения одной команды хранить в объекте команды можно, эту инициативу одобряю
        self.result = f'Операция {self.command} {self.args} успешно выполнена'
        return self.result


class BraNSh:
    """Объект оболочки для выполнения команд хранит историю последних выполненных команд, журналирует выполняемые команды."""

    # ИСПОЛЬЗОВАТЬ: это должен быть атрибут, ограничивающей размер контейнера с объектами последних команд
    __count = 50

    # КОММЕНТАРИЙ: неверно поняли объектную модель — объект оболочки должен обеспечивать обработку различных команд, а не одной за раз
    # КОММЕНТАРИЙ: посмотрите как работает командная строка cmd или интерпретатор python в интерактивном режиме: приложение запускается (создаётся объект), после чего (старт обработки) обрабатывает столько команд, сколько введёт пользователь (обработка команд), до команды на выход из приложения (конец обработки)

    def __init__(self, command: Optional[Command]):
        # УДАЛИТЬ: этих атрибутов здесь быть не должно
        self.command = command.command
        self.args = command.args
        # УДАЛИТЬ: этот атрибут не используется
        self.todo = False
        # ДОБАВИТЬ: а должен здесь быть атрибут для объекта контейнера, в котором должны храниться self.__class__.__count последних команд — а в параметрах конструктора следует прописать опциональный параметр для переопределения размера истории команд
        # ДОБАВИТЬ: также, должен быть атрибут для необходимости ведения журнала — и тоже опциональный параметр конструктора

    def start(self) -> None:
        """Запускает обработку команд."""
        # УДАЛИТЬ: что изменилось в поведении объекта оболочки с изменением этого атрибута? ничего
        self.todo = True
        # ДОБАВИТЬ: здесь вполне могут быть вывод строки с приветствием, версией приложения, вызов метода вывода справки — но главное, здесь должен быть вызов метода обработки

    def get_commands(self) -> Optional[str]:
        """Обрабатывает ввод команд и их аргументов."""
        # ДОБАВИТЬ: согласно условию, команды вы должны получать из стандартного потока ввода stdin — и реализовать такое поведение вы должны именно в данном методе

        # ДОБАВИТЬ: после ввода пользователем команды вы именно здесь создаёте экземпляр класса Command и дальше работаете именно с этим объектом, а не с отдельными строками имени команды и её аргументов — для этого вы класс Command объявляли — это, кстати, и будет композицией

        # ДОБАВИТЬ: далее вы здесь, проверяете, относится ли команда к управлению оболочкой (вкл./выкл. журналирования, справка, выход), если нет, то выполняете команду, используя её метод, добавляете команду в свой контейнер истории команд, проверяете необходимость журналирования и так далее

    def help(self) -> str:
        """Возвращает строку со справкой по использованию объекта оболочки."""
        # ИСПОЛЬЗОВАТЬ: при наличии строки документации, ключевое слово pass не требуется

    # ИСПОЛЬЗОВАТЬ: вы не хотите, чтобы логированием можно было управлять снаружи объявления класса, поэтому здесь целесообразно использование защищённого атрибута
    def __log(self) -> str:
        """Логирует выполняемые команды."""
        # ИСПРАВИТЬ: ведение журнала в файле никак не связано с хранением последних введённых команд
        self.__class__.__count += 1
        if self.__class__.__count < 51:
            file_name = 'log_command_f.txt'
            # ИСПРАВИТЬ: ключ параметра mode указывать не требуется; требуется указывать использование кодировки utf-8
            file = open(file_name, mode='a')
            log_data = f'{dt.now()} {self.command} {self.args}'
            file.write(f'{log_data}\n')
            # ДОБАВИТЬ: все файлопотоки должны быть закрыты сразу по окончании работы с файлом!
            return log_data
        else:
            self.__class__.__count = 1
            file_name = 'log_command_f.txt'
            file = open(file_name, mode='w')
            log_data = f'{dt.now()} {self.command} {self.args}'
            file.write(f'{log_data}\n')
            return log_data

    def exit(self) -> None:
        """Завершает обработку команд."""
        # УДАЛИТЬ: так ни разу и не был проверен
        self.todo = False
        # КОММЕНТАРИЙ: нигде не видел, чтобы оболочка командной строки перед закрытием выводила список всех введённых команд, но ваша воля — это хотя бы забавно
        print(self.command)
        # ИСПРАВИТЬ: exit — это функция
        exit


# КОММЕНТАРИЙ: в коде верхнего уровня мы должны создать экземпляр оболочки, после чего от этого экземпляра запустить обработку команд — всё остальное должен делать сам объект оболочки


# КОММЕНТАРИЙ: очень много противоречий между условием задачи, документацией, именами объектов и реализацией; я специально сначала переписал документацию и имена так, как у вас фактически написаны классы и методы — то есть, если бы они были верными, то документацию на них стоило бы писать именно так

# СДЕЛАТЬ: пишите документацию из головы, не старайтесь сэкономить время за счёт копирования огрызков условия — ваша задача заключается не в экономии времени, а в овладении принципами объектного проектирования и реализации — думайте, формулируйте, постоянно проверяйте себя

# КОММЕНТАРИЙ: если вам так будет проще мыслить, то представьте, что каждая ваша сдача домашнего задания — это презентация кода проверяющей комиссии в моём лице (плюс зрители в лице ваших одногруппников); а имена объектов, документация и комментарии в коде — это ваша речёвка; регламент никто не отменял, высказываться нужно ёмко и лаконично


# ИТОГ: перепроектировать объектную модель, переписать код и документацию — 3/10

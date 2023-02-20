# импорт из стандартной библиотеки
import builtins
from dataclasses import dataclass
from enum import Enum
from functools import partial
from re import match
from string import ascii_lowercase as a_lc
from typing import Optional

# импорт дополнительных модулей
import matrix


class SquareColor(int, Enum):
    """
    Цвет поля на доске.
    """
    LIGHT = 0
    DARK = 1

class PieceColor(Enum):
    """
    Цвет фигуры.
    """
    WHITE = 0
    BLACK = 1

class PieceKind(Enum):
    """
    Вид фигуры.
    """
    KING = 0
    QUEEN = 1
    ROOK = 2
    BISHOP = 3
    KNIGHT = 4
    PAWN = 5


@dataclass
class Piece:
    """
    Описывает сущность фигуры.
    """
    color: PieceColor
    kind: PieceKind
    square: Optional['Square']

    def __post_init__(self):
        self.removed: bool = False

    def __del__(self):
        """Удаляет фигуру с поля."""
        self.square.piece = None
        self.square = None
        self.removed = True

    def __repr__(self):
        return f'{self.color.name.title()} {self.kind.name.title()}'

    def __str__(self):
        return self.color.name[0] + self.kind.name[0]

    def move(self, end_square: 'Square') -> None:
        """Осуществляет проверку, ход фигуры и взятие фигуры противника."""
        if end_square.piece is not None:
            if end_square.piece.color is self.color:
                raise Exception
            else:
                del end_square.piece
        self.square.piece = None
        self.square = end_square
        end_square.piece = self


@dataclass
class Square:
    """
    Описывает сущность поля.
    """
    color: SquareColor
    file: str
    rank: str
    piece: Optional[Piece] = None

    def __repr__(self):
        return f'<{self.file + self.rank}: {self.piece!r}>'

    def __str__(self):
        return self.file + self.rank


class Chessboard(dict):
    """
    Описывает сущность игровой доски.
    """
    class File(dict):
        """
        Вертикаль игровой доски.
        """
        def __init__(self, file: str, start_color: SquareColor):
            super().__init__()
            for i in range(4):
                for j in range(2):
                    rank = i*2 + j + 1
                    self[rank] = Square(
                        list(SquareColor)[start_color-j],
                        file,
                        str(rank)
                    )

    def __init__(self):
        """Создаёт и нумерует игровою доску и заполняет её пустыми полями соответствующих цветов."""
        super().__init__()
        for i in range(8):
            for _ in range(4):
                for j in range(2):
                    self[a_lc[i]] = self.__class__.File(a_lc[i], list(SquareColor)[j-i%2])
        self.__post_init__()

    def __post_init__(self):
        """Расставляет фигуры на игровой доске в начальную позицию."""
        self['a1'].piece = Piece(PieceColor.WHITE, PieceKind.ROOK, self['a1'])
        self['b1'].piece = Piece(PieceColor.WHITE, PieceKind.KNIGHT, self['b1'])
        self['c1'].piece = Piece(PieceColor.WHITE, PieceKind.BISHOP, self['c1'])
        self['d1'].piece = Piece(PieceColor.WHITE, PieceKind.QUEEN, self['d1'])
        self['e1'].piece = Piece(PieceColor.WHITE, PieceKind.KING, self['e1'])
        self['f1'].piece = Piece(PieceColor.WHITE, PieceKind.BISHOP, self['f1'])
        self['g1'].piece = Piece(PieceColor.WHITE, PieceKind.KNIGHT, self['g1'])
        self['h1'].piece = Piece(PieceColor.WHITE, PieceKind.ROOK, self['h1'])
        for rank in a_lc[:8]:
            self[rank][2].piece = Piece(PieceColor.WHITE, PieceKind.PAWN, self[rank][2])
        self['a8'].piece = Piece(PieceColor.BLACK, PieceKind.ROOK, self['a8'])
        self['b8'].piece = Piece(PieceColor.BLACK, PieceKind.KNIGHT, self['b8'])
        self['c8'].piece = Piece(PieceColor.BLACK, PieceKind.BISHOP, self['c8'])
        self['d8'].piece = Piece(PieceColor.BLACK, PieceKind.QUEEN, self['d8'])
        self['e8'].piece = Piece(PieceColor.BLACK, PieceKind.KING, self['e8'])
        self['f8'].piece = Piece(PieceColor.BLACK, PieceKind.BISHOP, self['f8'])
        self['g8'].piece = Piece(PieceColor.BLACK, PieceKind.KNIGHT, self['g8'])
        self['h8'].piece = Piece(PieceColor.BLACK, PieceKind.ROOK, self['h8'])

        for rank in a_lc[:8]:
            self[rank][7].piece = Piece(PieceColor.BLACK, PieceKind.PAWN, self[rank][7])

    def __rank(self, number): # -> list[Square]:
        """Возвращает горизонталь игровой доски."""
        return [file[number] for file in self.values()]

    def __getitem__(self, key: str | int):
        """Обеспечивает вариативный доступ к полям игровой доски."""
        # ИСПОЛЬЗОВАТЬ: экземпляр Chessboard представляет из себя словарь, во время инициализации
        # он заполняется вертикалями экземплярами File с ключами от 'a' до 'h'; а метод __rank()
        # принимает int и возвращает горизонталь — переопределение __getitem__() нужно,
        # чтобы иметь возможность от экземпляра шахматной доски быстро получить доступ и к вертикали, и к горизонтали
        key = str(key).lower()
        if match(r'^[a-h][1-8]$', key):
            return super().__getitem__(key[0])[int(key[1])]
        elif match(r'^[a-h]$', key):
            return super().__getitem__(key)
        elif match(r'^[1-8]$', key):
            return self.__rank(int(key))
        else:
            raise KeyError

    def to_matrix(self):
        res = ()
        for i in range(8, 0, -1):
            res += (tuple(
                str(sq.piece) if sq.piece else ''
                for sq in self.__rank(i)
            ),)
        return matrix.Matrix(res)


class Turn:
    """
    Хранит информацию о сделанном ходе.
    """
    def __init__(self,
                 piece: Optional[Piece],
                 start_position: Optional[Square],
                 end_position: Optional[Square]):
        """
        :param piece: фигура
        :param start_position: начальное поле
        :param end_position: конечное поле .
        """
        self.piece = piece
        if self.piece:
            self.start_position = start_position
            self.end_position = end_position
        else:
            self.start = None
            self.end = None
        # ДОБАВИТЬ: на конечном поле тоже может быть фигура — неплохо было бы это учесть (см. комментарий 1 к выводу)

    def __str__(self):
        return f'{self.piece}{self.start_position}{self.end_position}'


# ДОБАВИТЬ: аннотации — везде
class Game:
    """
    Класс управляет игровым полем
    """
    def __init__(self):
        self._history = []
        self.board = Chessboard()
        self.elem = ''
        self.count = 0
        self.last_position = ''
        self.last_position_start = ''
        self.last_position_end = ''

    def move(self, start_position, end_position):
        """Сохраняет ход фигуры"""
        piece = self.board[start_position].piece
        if piece:
            piece.move(self.board[end_position])
            turn = Turn(piece, self.board[start_position], self.board[end_position])
            # ОТВЕТИТЬ: зачем счётчик ходов, если при отмене/возврате хода вы удаляете/добавляете последний элемент истории?
            # ИСПРАВИТЬ: сильно сомневаюсь, что строка, как элемент истории, лучше экземпляра Turn
            self.elem = turn
            # ИСПРАВИТЬ: зачем словарь, если ключами у вас выступают целые числа? для этого довольно и списка
            self._history.append(self.elem)

    def history(self):
        """Возвращает историю ходов"""
        return self._history

    def undo(self):
        """Возвращает фигуру на 1 ход назад"""
        if self.count > 0:
            self.last_position = self._history.pop(self.count)
            self.count -= 1
            # ИСПРАВИТЬ: очень грустная история: ставить реализацию команды в зависимость от человеко-читаемого строкового представления экземпляра хода — попробуйте ещё
            self.last_position_start = str(self.last_position)[2:4]
            self.last_position_end = str(self.last_position)[4:6]
            # ИСПРАВИТЬ: вот вроде бы и логично воспользоваться имеющимся методом, но обратили ли вы внимание,
            # что при этом у вас появляется в истории запись "хода наоборот"? это может добавить вам проблем впоследствии (см. комментарий 2 к выводу)
            self.move(self.board[self.last_position_end], self.board[self.last_position_start])
            piece = self.board[self.last_position_end].piece
            turn = Turn(piece, self.board[self.last_position_start], self.board[self.last_position_end])
            return turn
        return None

    def __str__(self):
        return matrix.draw_matrices(self.board.to_matrix(), outer_borders=True)

    # def redo(self):
    #     """Отменяет возврат фигуры на 1 ход"""
    #     self.move(self.board[self.last_position_start], self.board[self.last_position_end])
    #     piece = self.board[self.last_position_start].piece
    #     turn = Turn(piece, self.board[self.last_position_start], self.board[self.last_position_end])
    #     return turn



game = Game()
# УДАЛИТЬ: экземпляр доски у вас уже есть в соответствующем атрибуте экземпляра игры


print('Игровое поле:')

# ИСПОЛЬЗОВАТЬ: новое значение по умолчанию для параметров sep и end функции print — чтобы не прописывать в каждом последующем print переопределения
print = partial(print, sep='\n', end='\n\n')

# КОММЕНТАРИЙ: подумайте над ним в задании 10.09
# над визуалом игрового поля еще думаю

# ИСПРАВИТЬ: именно для того, чтобы спокойно передавать сюда строки, я и прописывал __getitem__() в Chessboard
game.move(game.board["e2"], game.board["e4"])
game.move(game.board["e7"], game.board["e5"])
game.move(game.board["d1"], game.board["h5"])
# КОММЕНТАРИЙ: далековато коняга ускакал за один ход =) следующее задание как раз такие ходы должно проверять
game.move(game.board["g8"], game.board["c6"])
game.move(game.board["h5"], game.board["f7"])

print(game)
print(game.history())
game.undo()
print('Отмена хода:', game)
print(game.history())
#game.redo()
print('Возврат хода:', game.history())


# ИСПОЛЬЗОВАТЬ: возврат к встроенному вызываемому объекту print с его исходными значениями по умолчанию
# print = builtins.print

# Игровое поле:
#  —————————————————————————————————————————
#  | BR | BK | BB | BQ | BK | BB |    | BR |
#  —————————————————————————————————————————
#  | BP | BP | BP | BP |    | WQ | BP | BP |
#  —————————————————————————————————————————
#  |    |    | BK |    |    |    |    |    |
#  —————————————————————————————————————————
#  |    |    |    |    | BP |    |    |    |
#  —————————————————————————————————————————
#  |    |    |    |    | WP |    |    |    |
#  —————————————————————————————————————————
#  |    |    |    |    |    |    |    |    |
#  —————————————————————————————————————————
#  | WP | WP | WP | WP |    | WP | WP | WP |
#  —————————————————————————————————————————
#  | WR | WK | WB |    | WK | WB | WK | WR |
#  —————————————————————————————————————————
#
# {1: 'WPe2e4', 2: 'BPe7e5', 3: 'WQd1h5', 4: 'BKg8c6', 5: 'WQh5f7'}
#
# Отмена хода:
# КОММЕНТАРИЙ 1: здесь видно, что чёрная пешка (BP) на f7, взятая белым ферзём (WQ), не восстановилась после отмены хода
#  —————————————————————————————————————————
#  | BR | BK | BB | BQ | BK | BB |    | BR |
#  —————————————————————————————————————————
#  | BP | BP | BP | BP |    |    | BP | BP |
#  —————————————————————————————————————————
#  |    |    | BK |    |    |    |    |    |
#  —————————————————————————————————————————
#  |    |    |    |    | BP |    |    | WQ |
#  —————————————————————————————————————————
#  |    |    |    |    | WP |    |    |    |
#  —————————————————————————————————————————
#  |    |    |    |    |    |    |    |    |
#  —————————————————————————————————————————
#  | WP | WP | WP | WP |    | WP | WP | WP |
#  —————————————————————————————————————————
#  | WR | WK | WB |    | WK | WB | WK | WR |
#  —————————————————————————————————————————
#
# {1: 'WPe2e4', 2: 'BPe7e5', 3: 'WQd1h5', 4: 'BKg8c6', 5: 'WQf7h5'}
#
# Возврат хода:
# КОММЕНТАРИЙ 2: пример потенциальной проблемы с добавлением в историю "хода наоборот" после стирания исходного
# {1: 'WPe2e4', 2: 'BPe7e5', 3: 'WQd1h5', 4: 'BKg8c6', 5: 'WQf7h5', 6: 'WQh5f7'}


# ИТОГ: для черновика неплохо, но нужно дорабатывать — 5/12

# СДЕЛАТЬ: работу над ошибками и сообщить мне об этом

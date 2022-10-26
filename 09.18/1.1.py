# Магический квадрат - матрица чисел, в которой сумма чисел любой строки, столбца или диагонали одинакова.
# Вам даётся проект из трёх классов, которые могут быть использованы для построения магического квадрата.
# Это классы:
#   Generator: этот класс генерирует список из девяти случайных чисел
#   Splitter: это класс, который принимает двумерный список и разбивает его на все возможные одномерные списки. Он даёт в результате колонки, строки и две диагонали.
#   Verifier: этот класс принимает двумерный список и проверяет, что сумма чисел любого из содержимых списков одинакова.
# Вам только остаётся реализовать фасад, названный MagicSquareGenerator который генерирует магический квадрат заданного размера.

from random import randint


class Generator:
    @staticmethod
    def generate(count: int):
        return [randint(1,9) for _ in range(count)]


class Splitter:
    @staticmethod
    def split(array) -> list:
        result = []

        row_count = len(array)
        col_count = len(array[0])

        for r in range(row_count):
            the_row = []
            for c in range(col_count):
                the_row.append(array[r][c])
            result.append(the_row)

        for c in range(col_count):
            the_col = []
            for r in range(row_count):
                the_col.append(array[r][c])
            result.append(the_col)

        diag1 = []
        diag2 = []

        for c in range(col_count):
            for r in range(row_count):
                if c == r:
                    diag1.append(array[r][c])
                r2 = row_count - r - 1
                if c == r2:
                    diag2.append(array[r][c])

        result.append(diag1)
        result.append(diag2)

        return result


class Verifier:
    @staticmethod
    def verify(arrays) -> bool:
        first = sum(arrays[0])

        for i in range(1, len(arrays)):
            if sum(arrays[i]) != first:
                return False

        return True


class MagicSquareGenerator:
    # ИСПРАВИТЬ: если вы пишете комментарий, то размещайте его над комментируемой строкой; так, этот комментарии разумнее отнести к атрибуту
    # num - размерность матрицы
    def __init__(self, num):
        # ИСПОЛЬЗОВАТЬ: если же вы хотите описать параметры метода, то это можно сделать в строке документации:
        """
        :param num: размерность матрицы
        """
        self.generator = Generator()
        self.splitter = Splitter()
        self.verifier = Verifier()
        self.num = num

    def make_magic_square(self):
        # ИСПРАВИТЬ: документацию метода или функции принято начинать с глагола и писать так, чтобы первое предложение документации отвечало на вопрос "что делает метод/функция?"
        """выводит магический квадрат"""
        while True:
            self.array = [
                self.generator.generate(self.num)
                # ИСПОЛЬЗОВАТЬ: в случаях, когда мы не используем переменную цикла, мы можем в качестве имени использовать символ подчёркивания
                for _ in range(self.num)
            ]
            if self.verifier.verify(self.splitter.split(self.array)):
                return self.array


magic = MagicSquareGenerator(3)
magic_square = magic.make_magic_square()
for elem in magic_square:
    print(elem)


# ДОБАВИТЬ: под меткой tests закомментированные результаты выполнения скрипта с различными входными данными
# tests:
# [6, 1, 8]
# [7, 5, 3]
# [2, 9, 4]
###########
# [4, 1, 4]
# [3, 3, 3]
# [2, 5, 2]

# ИТОГ: не хватает только тестов, остальное отлично — 5/6

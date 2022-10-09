import re


class TextParser:
    """Парсер текстовых данных в некой системе."""

    def __init__(self, text: str):
        tmp = re.sub(r'\W', ' ', text.lower())
        tmp = re.sub(r' +', ' ', tmp).strip()
        self.text = tmp

    def get_processed_text(self, processor) -> None:
        """Вызывает метод класса обработчика.

        :param processor: экземпляр класса обработчика
        """
        result = processor.process_text(self.text)
        print(*result, sep='\n')


class WordCounter:
    """Счётчик частотности слов в тексте."""

    def __init__(self, text: str) -> None:
        """Обрабатывает переданный текст и создаёт словарь с частотой слов."""
        self.__words = dict()
        for word in text.split():
            self.__words[word] = self.__words.get(word, 0) + 1

    def get_count(self, word: str) -> int:
        """Возвращает частоту переданного слова."""
        return self.__words.get(word, 0)

    def get_all_words(self) -> dict[str, int]:
        """Возвращает словарь с частотой слов."""
        return self.__words.copy()


class TextAdapter:
    """Адаптер к обработчику"""

    def __init__(self, adapter: WordCounter):
        self.adapter = adapter

    def process_text(self, text):
        """ Интерфейс обработчика, требуемого системой"""
        words = self.adapter.get_all_words().items()
        return words


text = 'kk la text test test'
parser = TextParser(text)
counter = WordCounter(text)
adapter = TextAdapter(counter)
parser.get_processed_text(adapter)


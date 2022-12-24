"""Контроллер MVC."""

# КОММЕНТАРИЙ: при импорте модулей своего проекта желательно использовать инструкцию import, а не from...import... — это уменьшает вероятность закольцовывания импорта
# УДАЛИТЬ: экземпляр контроллера должен получать необходимые объекты в конструкторе, следовательно вам не нужны эти импорты здесь — для этого создавался модуль входа
import model
import view

from enum import Enum

class UserAnswer(str, Enum):
    YES = 1
    NO = 0


class Application:
    """Контроллер"""

    def __init__(self, view: 'CLIView', model:'Email'):
        self.view = view
        self.model = model
        self.em = None

    def start(self) -> None:
        """Старт приложения"""
        self.view.start()
        self.check_email()

    def check_email(self) -> None:
        """Проверяет email на корректность"""
        try:
            self.em = self.model(self.view.input_email())
            self.view.answer()
            self.save_email()

        except ValueError:
            self.view.mistake()
            self.check_email()

    def save_email(self) -> None:
        """Записывает в файл"""

        save_or_not = input("Сохранить?\n").lower()
        if save_or_not == UserAnswer.YES.value:
            self.em.save()
        save_or_not = input("Продолжить?\n").lower()
        if save_or_not == UserAnswer.YES.value:
            self.check_email()
        else:
            self.end()

    def end(self) -> None:
        """Завершает работу"""

        self.view.end_view()


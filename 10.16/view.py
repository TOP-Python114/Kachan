"""Представление MVC."""

class CLIView:

    @staticmethod
    def start() -> None:
        """Приветствует в приложении"""
        print('Добрый день!')

    @staticmethod
    def input_email() -> str:
        email = input('Введите почту\n')
        return email

    @staticmethod
    def invalid_email() -> None:
        """Сообщает об ошибке"""
        print('Почта введена некорректно')

    # ДОБАВИТЬ: вывод вопросов о сохранении и продолжении, получение соответствующего ввода

    @staticmethod
    def valid_email() -> None:
        """Сообщает об отсутствии ошибок"""
        print('Ошибок не обнаружено')

    @staticmethod
    def end_view() -> None:
        """Сообщает о завершении работы"""
        print('До свидания')




def log_errors(func_new):

    """Декоратор, который который логирует вызов функции в файл-журнал, используя атрибуты объекта функции __name__ и аргументы, переданные функции"""

    def wrapper(a, b):
        result = func_new(a, b)
        file_name = 'function_errors.log'
        file = open(file_name, mode='a')
        file.write(f'Функция: {func_new.__name__} \n {a} \n {b} \n')
        return result
    return wrapper


@log_errors
def checkhand(a, b):

    return a - b


print(checkhand(10, 0))



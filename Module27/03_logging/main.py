from datetime import datetime
from time import sleep
import functools
from typing import Callable, Any


def logging(func: Callable) -> Callable:
    """Декоратор. Логирует ошибки функций с указанием даты и времени возникновения."""

    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        try:
            print(f'{func.__name__}\n{func.__doc__}')
            function = func(*args, **kwargs)
            return function
        except Exception as exc:
            string = '{} - {}:\t{}\n'.format(datetime.now(), func.__name__, exc)
            with open('function_errors.log', 'a', encoding='utf-8') as log:
                log.write(string)

    return wrapped_func


@logging
def division_by_zero():
    """Деление на нуль."""
    sleep(1)
    raise ZeroDivisionError('Деление на ноль')


@logging
def value_error():
    """Вызывает ValueError."""
    sleep(1)
    raise ValueError('Неверное значение')


@logging
def name_error():
    """Вызывает NameError."""
    sleep(1)
    raise NameError('Неверное имя')


@logging
def index_error():
    """Вызывает IndexError."""
    sleep(1)
    raise IndexError('Нет такого индекса')


division_by_zero()
value_error()
name_error()
index_error()

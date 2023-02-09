import functools
from typing import Callable, Any, Optional


def callback(route: str) -> Callable:
    """Декоратор. выполняется после определённого события"""
    def inner_decorator(func: Callable) -> Callable:
        app[route] = func # это событие о котором идет речь??

        @functools.wraps(func)
        def wrapped() -> Any:
            return func()
        return wrapped
    return inner_decorator


app = {}


@callback('//')
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')

print(f'Словарь: {app}')
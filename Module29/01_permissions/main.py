import functools
from typing import Callable, Any, Optional


def check_permission(user: str) -> Callable:
    """Декоратор, проверяет права доступа для выполнения функции"""
    def inner_decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapped() -> Any:

            if user in user_permissions:
                return func()
            print(f'PermissionError: У пользователя {user} недостаточно прав, '
                  f'чтобы выполнить функцию {func.__name__}')
        return wrapped
    return inner_decorator


user_permissions = ['admin']


@check_permission('admin')
def delete_site():
    print('Удаляем сайт')

@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()
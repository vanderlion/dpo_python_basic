from typing import Callable
import functools

class CountCalls:
    """Класс декоратор. Считает количество вызовов функции
        метод num_calls для базовой функции для счета вызовов
    """
    def __init__(self, func: Callable) -> None:

        functools.update_wrapper(self, func)
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs) -> Callable:
        self.num_calls += 1
        print(f'Вызов номер {self.num_calls} функции: {self.func.__name__}')
        return self.func(*args, **kwargs)


@CountCalls
def say_hello():
    print('Hello')


say_hello()
say_hello()
say_hello()
print(say_hello.num_calls)
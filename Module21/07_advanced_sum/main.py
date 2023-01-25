from typing import Iterable


def sum_(*args):
    return sum(sum_(*arg) if isinstance(arg, Iterable) else arg for arg in args)


print(sum_([[1, 2, [3]], [1], 3]))
print(sum_(1, 2, 3, 4, 5))
import time
from typing import Callable, Any


def waiting(func: Callable) -> Callable:
    def timing() -> Any:
        print('Downloding... Wait!')
        time.sleep(3)
        func()
    return timing

@waiting
def test():
    print('Complete!')

test()


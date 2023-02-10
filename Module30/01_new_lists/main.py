from typing import List
from functools import reduce
 
floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]
 
""" Каждое число из списка floats возводится в третью степень и округляется до трёх знаков после запятой"""
result = map(lambda x: round(x ** 3, 3), floats)
print(list(result))
 
"""Из списка names берутся только те имена, в которых есть минимум пять букв """
 
result = filter(lambda elem: len(elem) >= 5, names)
print(list(result))
 
""" Из списка numbers берётся произведение всех чисел """


def my_add(a: int, b: int) -> int:
    return a * b


result = reduce(my_add, numbers)
print(result)

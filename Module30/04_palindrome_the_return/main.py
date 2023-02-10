from collections import Counter
# возвращает словарь ключ-символ, значение - количество


def can_be_poly(string: str) -> bool:
    """ функция can_be_poly, которая принимает на вход строку
        и проверяет, можно ли получить из неё палиндром """
    return len(string) % 2 == sum(x % 2 for x in Counter(string).values())
    return len(list(filter(lambda x: x % 2, Counter(string).values()))) <= 2
    return list(filter(lambda x: x % 2, Counter(string).values()))


print(can_be_poly('abcba'))
print(can_be_poly('abbbc'))
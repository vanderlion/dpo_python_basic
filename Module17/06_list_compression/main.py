import random

n = input("Кол-во чисел в списке: ")
list1 = [random.randint(0, 2) for _ in range(int(n))]
print("Список до сжатия:", list1)
list2 = [x for x in list1 if x]
print("Список после сжатия: ", list2)
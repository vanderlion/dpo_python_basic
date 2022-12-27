first_list = []
second_list = []

for i in range(1, 4):
    print('Введите', i, 'число для первого списка:', end=' ')
    number = int(input())
    first_list.append(number)

for i in range(1, 8):
    print('Введите', i, 'число для второго списка:', end=' ')
    number = int(input())
    second_list.append(number)

first_list.extend(second_list)
for _ in range(len(first_list)):
    for i in first_list:
        if first_list.count(i) > 1:
            first_list.remove(i)
print(first_list)
print(second_list)
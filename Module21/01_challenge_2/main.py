def all_num(num):
    if num != 0:
        all_num(num - 1)
        print(num)

number = int(input('Введите num: '))
all_num(number)
import random

numbers_list = []
work = True
def do_it():
    sum = 0
    number = int(input("Введите число: "))
    if (len(numbers_list) > 0):
        n = random.randint(1,13)
        if (n==13):
            print('Вы потерпели неудачу')
            exit()
        else:
            numbers_list.append(number)
        for i in range(0, len(numbers_list)):
            sum = sum + numbers_list[i];
            if (sum >= 777):
                print('Вы успешно выполнили условие для выхода из порочного цикла!')
                work = False
                with open('out_file.txt', 'w') as f:
                    f.writelines(str(numbers_list) + '\n')
                exit()
    else:
        numbers_list.append(number)

while (work):
    do_it()
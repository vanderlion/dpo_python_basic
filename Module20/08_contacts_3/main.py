l = ['Введите имя и фамилию нового контакта (через пробел): ', 'Введите номер телефона: ']
d = {}

while True:
    print('Введите номер действия:\n')
    print('1. Добавить контакт')
    print('2. Найти человека')
    a = input('-> ')

    if a == '1':
        ss = str()
        for i in l:
            s = input(i)
            ss += ' ' + s
        ss = ss.split()
        key = (ss[0], ss[1])
        if key in d:
            print('Такой человек уже есть в контактах.')
        else:
            d[key] = ss[2]
            print('Текущий словарь контактов:', d)

    if a == '2':
        a = input('-> ')
        for k in d.keys():
            if a == k[1]:
                print(k[0], k[1], d[k])
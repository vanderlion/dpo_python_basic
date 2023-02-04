def QHofstadter(s):
    if s == [1, 1]:
        a = s[:]
        while True:
            try:
                q = a[-a[-1]] + a[-a[-2]]
                a.append(q)
                yield q
            except IndexError:
                return
    else:
        print('Передано неверное значение списка!\nПравильный список [1, 1]')


Q = [1, 1]

for i, number in enumerate(QHofstadter(Q)):
    if i <= 30:
        print(number, end=', ')
    else:
        break

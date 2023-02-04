list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
to_find = 56


def func(to_find):
    for x in list_1:
        for y in list_2:
            result = x * y
            yield x, y, result
            if result == to_find:
                print('Found!!!')
    return


for num in func(to_find):
    print(str(num)[1:-1])
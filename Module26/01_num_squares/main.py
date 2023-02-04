class MyItter:
    def __init__(self, number):
        self.count = 0
        self.number = number

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        if self.count == self.number:
            raise StopIteration
        else:
            return self.count ** 2


user = int(input("Введите число: "))
my_itter = MyItter(number=user)

for i_elem in my_itter:
    print(i_elem, end=' ')
print()


def gen_func(number):
    for i_num in range(number):
        yield i_num ** 2


user = int(input("Введите число: "))

gen = gen_func(user)
for i_elem in gen:
    print(i_elem, end=' ')
print()
user = int(input("Введите число: "))
gen = (i_elem ** 2 for i_elem in range(user))

for i in gen:
    print(i, end=' ')





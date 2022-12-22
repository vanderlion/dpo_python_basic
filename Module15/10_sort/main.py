x = []
N = int(input("Введите кол-во чисел для сортировки"))
for i in range(N):
    k = int(input("Введите число: "))
    x.append(k)
print (sorted(x))
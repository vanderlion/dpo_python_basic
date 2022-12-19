def find_monetka(c1,c2,r):
    if (c1 ** 2 + c2 ** 2) ** 0.5 <= r:
        print("Монетка где-то рядом")
    else:
        print("Монетки в области нет")
x_m=float(input("Введите координату x: "))
y_m=float(input("Введите координату y: "))
r=int(input("Введите радиус r: "))
find_monetka(x_m, y_m, r)

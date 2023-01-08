sticks = list("I" * int(input("Количество палок: ")))

for i in range(1, int(input("Количество бросков: ")) + 1):
    for j in range(int(input(f"Бросок {i}. Палки сбиты с номера: ")) - 1, int(input("по номер "))):
        sticks[j] = ". "
print("Результат:", "".join(sticks))
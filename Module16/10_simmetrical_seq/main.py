N = int(input("Кол-во чисел: "))
number_list = []
reverse_number_list = []

for _ in range(N):
    number = int(input("Число: "))
    number_list.append(number)

print("\nПоследовательность: ", number_list)

for index in range(len(number_list) - 1, -1, -1):
    reverse_number_list.append(number_list[index])
    print(reverse_number_list)

while True:
    if number_list[len(number_list) - 1] == reverse_number_list[0]:
        reverse_number_list.remove(reverse_number_list[0])
    else:
        break

print("Нужно приписать чисел: ", len(reverse_number_list))
print("Сами числа: ", reverse_number_list)
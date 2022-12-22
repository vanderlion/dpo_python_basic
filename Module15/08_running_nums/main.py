N = int(input("Кол-во элементов: "))
start_list = []
finish_list = []

for _ in range(N):
    element = input("Введите элемент списка:")
    start_list.append(element)

K = int(input("Сдвиг: "))
index = 0
while index < N - 1:
    empty_place = start_list[index]
    start_list[index] = start_list[index - K]
    start_list[index - K] = empty_place
    index += 1

print(start_list)
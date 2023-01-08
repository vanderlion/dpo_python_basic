import random
list_1 = [round(random.uniform(5, 10), 2) for x in range(20)]
list_2 = [round(random.uniform(5, 10), 2) for x in range(20)]
list_3 = [(list_1[i_num] if list_1[i_num] > list_2[i_num]
else list_2[i_num]) for i_num in range(20)]
print("Первая команда: ", list_1)
print("Вторая команда: ", list_2)
print("Победители тура: ", list_3)
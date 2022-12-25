violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]


li = []
special_list = []
qty = int(input('Сколько песен выбрать? '))
print()
count = 1

for _ in range(qty):
    song = input('Введите название ' + str(count) + ' песни: ')
    for elem in violator_songs:
        li.extend(elem)
        if song not in li:
            print('Ошибка. Такой песни в плейлисте нет!')
            break
        else:
            special_list.append(song)
            count += 1
            summ = 0
for i_time in violator_songs:
    if i_time[0] in special_list:
        summ += i_time[1]
print('\nОбщее время звучания песен:', float(round(summ, 2)))
violator_songs = [
    ["World in My Eyes", 4.86],
    ["Sweetest Perfection", 4.43],
    ["Personal Jesus", 4.56],
    ["Halo", 4.9],
    ["Waiting for the Night", 6.07],
    ["Enjoy the Silence", 4.20],
    ["Policy of Truth", 4.76],
    ["Blue Dress", 4.29],
    ["Clean", 5.83]
]

custom_songs = []
songs = int(input("Сколько песен выбрать? "))
summ = 0
for i in range(songs):
    song = input('Введите название ' + str(i + 1) + ' песни: ')
    custom_songs.append(song)
for k in violator_songs:
    if k[0] in custom_songs:
        summ += k[1]
print("\nОбщее время звучания песен:", float(round(summ, 2)))
guest_counts=5
guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
while True:
    guest=input('Гость пришел или ушел?: ')
    name=input('Введите имя гостя: ')

    if guest=='пришел':
        print('Привет',name)
        guests.append(name)
        print('Сейчас на вечеринке',guest_counts+1, 'человек',guests)
        guest_counts+1

    if guest=='ушел':
        print('Пока',name)
        print('Сейчас на вечеринке',guest_counts-1, 'человек ',guests)
        guests.remove(1)
        guest_counts-=1

    if guest=='пора спать':
        print('Вечеринка закончилась, все легли спать')
    break
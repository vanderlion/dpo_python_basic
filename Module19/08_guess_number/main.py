numbers_count = int(input('Введите максимальное число: '))
numbers_dict = {str(dict_num): 'Нет' for dict_num in range(1, numbers_count + 1)}

while True:
    boris_phrase = input('Нужное число есть среди этих чисел: ')
    if boris_phrase == 'Помогите!':
        print('Артём мог загадать следующие числа:', end='')
        for number in numbers_dict.items():
            if number[1] == 'Да':
                print(number[0], end='')
        break
    else:
        boris_phrase.split()
        artems_answer = input('Ответ Артёма: ')
        for number in numbers_dict:
            if number in numbers_dict:
                print(number)
                numbers_dict[number] = artems_answer
    print(numbers_dict)
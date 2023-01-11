ls = input('Введите текст: ').split(' ')
max_len = max([len(x) for x in ls])
print("Самое длинное слово", [x for x in ls if len(x) == max_len], "\nДлина этого слова:", max_len)

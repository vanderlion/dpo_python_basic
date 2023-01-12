def zip_encode(target: str) -> str:
    result = ''
    counter = 0
    for i, char in enumerate(target):
        counter += 1
        if len(target) - 1 == i or char != target[i + 1]:
            result += f'{char}{counter}'
            counter = 0
    return result


text = input('Введите строку: ')
encoded = zip_encode(text)
print(encoded)

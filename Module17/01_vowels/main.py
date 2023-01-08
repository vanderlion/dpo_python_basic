vowels = "аоиеёэыуюя"

text = input("Введите текст: ")
letters = [c for c in text if c in vowels]

print("Список гласных букв:", letters)
print("Длина списка:", len(letters))
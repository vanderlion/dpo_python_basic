document = input("Название файла: ")

if document.startswith(("@", "№", "$", "%", "^", "&", "*", "(", ")")):
    print("Ошибка: название начинается на один из специальных символов")
elif not document.endswith('.txt') or document.endswith('.docx'):
    print("Ошибка: неверное расширение файла. Ожидалось .txt или .docx")
else:
    print("Файл назван верно", document)
text = open("zen.txt").read().lower()
letters = [c for c in text if c in "abcdefghijklmnopqrstuvwxyz"]
print("Количество букв в файле: ", len(letters),
      "Количество слов в файле: ", len(text.split()),
      "Количество строк в файле :", len(text.split("\n")),
      "Наиболее редкая буква: ", min(letters, key=letters.count), sep="\n")
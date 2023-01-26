import zipfile

dictionary = {}
with zipfile.ZipFile("voyna-i-mir.zip") as archive:
    for filename in archive.filelist:
        with archive.open(filename) as file:
            for letter in file.read().decode():
                if letter not in dictionary:
                    dictionary[letter] = 0
                dictionary[letter] += 1

for letter, amount in dictionary.items():
    print(letter, amount)
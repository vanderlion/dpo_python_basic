import os
import sys
from pathlib import Path

line, path, filename = str(input('Введите строку: ')), list(map(str, input('Куда хотите сохранить документ? Введите последовательность папок (через пробел):').split(' '))), str(input('Введите имя файла:'))
path = Path('/'.join(path))

try:
    if path.exists():
        os.chdir(path)
        path = Path(filename)
        if path.is_file():
            while True:
                try:
                    a = input('Overwrite file?\n')
                    if a == 'no':
                        print('File is not record')
                        break
                    if a == 'yes':
                        print(line, file=open(filename, 'w'))
                        print('Ok!')
                        break
                except KeyboardInterrupt:
                    print('Exit...')
                    break
                else:
                    print("No valid input!!!")
        else:
            print(line, file=open(filename, 'w'))
            print('File saved successfully!')
    else:
        print('Input correct path', file=sys.stderr)
except FileNotFoundError:
    print('No empty filename', file=sys.stderr)
except:
    print(sys.exc_info()[:2])
with open('numbers.txt') as file:
    for line in file.read().splitlines():
        print(sum(map(int, line.split())))
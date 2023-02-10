letters = ['a', 'b', 'c', 'd', 'e']
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

results = map(lambda x, y: (x, y), letters, numbers)
print(list(results))
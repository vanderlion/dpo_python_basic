print(*range(1,1001))

print([x for x in range(1, 1001) if all(x % d != 0 for d in range(2, int(x ** 0.5) + 1))])
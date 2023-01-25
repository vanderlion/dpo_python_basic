def calc_func(num, fact={0: 1}):
    if num not in fact:
        i = max(fact)
        for j in range(i + 1, num + 1):
            fact[j] = fact[j - 1] * j
    return pow(fact[num] / pow(num, 3), 10)


print(calc_func(10))
print(calc_func(21))

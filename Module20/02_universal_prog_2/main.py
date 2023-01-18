def crypto(checking_list):
    return [v for i, v in enumerate(checking_list) if i >= 2 and is_prime(i)]

def is_prime(i_num):
    k = 0
    for i in range(2, i_num // 2 + 1):
        if i_num % i == 0:
            k = k + 1
    if k <= 0:
        return True
    else:
        return False

print(crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(crypto('О Дивный Новый мир!'))

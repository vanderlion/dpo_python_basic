def calculating_math_func(data):
    if data in factorials:
        result = factorials[data]
    else:
        result = 1
        for index in range(1, data + 1):
            result *= index
        factorials[data] = result
    result /= data ** 3
    result = result ** 10
    return result


factorials = {}
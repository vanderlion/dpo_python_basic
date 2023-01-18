def slicer(x):
    for num in x:
        try:
            b = int(num)
            if b != num: return x
        except: return x
    num = list(x)
    num.sort()
    return tuple(num)

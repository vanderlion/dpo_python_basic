def slicer(t, num):
    if num not in t:
        return ()
    if t.count(num) == 1:
        return t[t.index(num):]
    return t[t.index(num):t.index(num, t.index(num) + 1) + 1]

print(slicer((1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10), 2))
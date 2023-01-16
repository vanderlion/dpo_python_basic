from collections import Counter
s = 'howmanytimes'
d = dict()
for k, v in Counter(s).items():
    d.setdefault(v, []).append(k)
print(d)
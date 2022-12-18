p=[]
for i in range(int(input('Перый год? ')),int(input('Второй год? '))+1):
    l=list(str(i))
    s=set(l)
    if len(s)==2:
        for j in s:
            if l.count(j)!=2: p.append(i); break
print (*p, sep='\n')

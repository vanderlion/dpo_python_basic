import re
lst = re.findall(r"[\w']+|[-.,!; ]", input("Сообщение: "))
print("Новое сообщение: ", *[s[::-1] for s in lst], sep = '')
n = input("Введите строку: ")
first_h = n.index("h")
last_h = n.rindex("h")
print("Развёрнутая последовательность между первым и последним h: ",
      n[last_h-1:first_h:-1])

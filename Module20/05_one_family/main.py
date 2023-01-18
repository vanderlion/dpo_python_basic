all_families_dict = {

1: {

"Питонов Никита": 35,

"Питонова Алина": 34,

"Питонов Павел": 10

},

2: {

"Програмистов Акакий": 115,

"Програмистова Зульфия": 112,

"Програмистов Корнеплод": 9,

"Програмистова Кочебрыжка": 10

}

}



family = input("Введите фамилию: ")

if list(family)[-1] == 'a':
    family = family[::-1]

print(family)
for key in all_families_dict.keys():
    for values in all_families_dict[key].keys():
        if family[:-1] in values:
            print(values, " ", all_families_dict[key][values])
def tpl_sort(incoming_list):
    my_list = list(incoming_list)
    return tuple(sorted(my_list))

print(tpl_sort((6, 3, -1, 8, 4, 10, -5)))
nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]


def flat(nested_list, one_dimensional_list = []):
    for item in nested_list:
        if isinstance(item, list):
            flat(item)
        else:
            one_dimensional_list.append(item)
    return one_dimensional_list

print(flat(nice_list))

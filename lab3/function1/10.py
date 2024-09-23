def unique_elements(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list


lst = [1, 2, 3, 2, 1, 5, 6, 5, 7, 8, 7]
print(unique_elements(lst))
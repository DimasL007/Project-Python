def remove_duplicates(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

def sort_list(input_list):
    return sorted(input_list, key=lambda x: (isinstance(x, str), x.lower() if isinstance(x, str) else x))

my_list = [1, 2, 3, 4, 5, 6, 3, 4, 5, 7, 6, 5, 4, 3, 4, 5, 4, 3, 'Привіт', 'анаконда']

unique_list = remove_duplicates(my_list)

sorted_list = sort_list(unique_list)

print(sorted_list)

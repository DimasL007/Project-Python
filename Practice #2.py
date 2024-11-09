name = "Dmytro"
surname = "Lyniuk"
age = 17
count_int = 0
count_str = 0
count_bool = 0
count_set = 0
count_list = 0
count_tuple = 0
count_float = 0
lst_notnull = []
max_value = -1
types_count = {str, int, bool, set, list, tuple, float}
lst_count_types = [count_set, count_float, count_tuple, count_list, count_bool, count_str, count_int]
lst_name_type = ['set', 'float', 'tuple', 'list', 'bool', str, int]
lst = [name, surname, age]
for iteml in lst:
    if type(iteml) == int:
        lst_count_types[-1] += 1
    elif type(iteml) == str:
        lst_count_types[-2] += 1

for itemc in lst_count_types:
    if itemc != 0:
        lst_notnull.append(itemc)
    if len(lst_notnull) == 0:
        print('Good')
    else:
        if itemc == max_value:
            print('Not')
            break

        elif itemc > max_value:
            max_value = itemc

inn = lst_count_types.index(max_value)

print(lst_name_type[inn])

for iteml in lst:
    if type(iteml) != lst_name_type[inn]:
        lst.remove(iteml)

lst = [1, 2, 3, 4, 5, 6, 3, 4, 5, 7, 6, 5, 4, 3, 4, 5, 4, 3, 11, 5, 7, 8, 0, 1, 7, 8, 9, 12, 7, 6, -2, 'Привіт', 'Анаконда']

# Функція видалення дублікатів
def def_lst_unique(lst):
    lst_unique = []  # Зберігає унікальні значення
    lst_in_set = set()  # Використовується для перевірки на унікальність
    for item in lst:
        item = item.lower() if type(item) == str else item  # Рядки переводимо в малий регістр якщо item є str

        if item not in lst_in_set: #Чи Немає item в lst_in_set
            lst_unique.append(item)  # Додаємо унікальний елемент до списку
            lst_in_set.add(item)  # Помічаємо цей елемент як оброблений
        return lst_unique  # Повертаємо список без дублікатів

# Функція сортування списку
def def_lst_sort(lst):
    lst_str = [k for k in lst if type(k) == str]  # Створюємо список для всіх елементів, які є рядками
    lst_int = [k for k in lst if type(k) == int]  # Створюємо список для всіх елементів, які є числами (цілими числами)
    # Сортуємо числа окремо, потім рядки, після чого об'єднуємо ці два списки
    return sorted(lst_int) + sorted(lst_str)  # Сортування чисел і рядків окремо, потім об'єднання

# Видаляємо дублікати та сортуємо
r = def_lst_unique(lst)  # Отримуємо список без дублікатів
sorted_list = def_lst_sort(r)  # Сортуємо список

print(sorted_list)  # Вивід Сортованого Списку

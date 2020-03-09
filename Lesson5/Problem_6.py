# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.

# Создаем список из строк файла
with open('Lesson6.txt', 'r') as f_objects:
    l_objects = f_objects.readlines()


def didgits_of_string(i_string: str):
    """Функция возвращает сумму чисел из исходной строки
       Корректно работает если в каждом слове строки только одно число
    """
    words = i_string.split()  # Разобьем входную строку на слова
    digit_list = []  # Выходной Список чисел
    for word in words:
        s_didgit = ''
        for symbol in word:
            if symbol.isdigit():
                s_didgit += symbol
        try:
            digit_list.append(int(s_didgit))
        except:
            pass
    return digit_list


d_objects = {}  # Наш словарь предметов
for object in l_objects:
    d_objects[object[:object.index(':')]] = sum(didgits_of_string(object[object.index(':') + 1:]))

print(d_objects)

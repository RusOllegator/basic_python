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

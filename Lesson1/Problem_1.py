# Вносим данные и выводим на экран

name = ''  # Имя
age = None  # Возвраст лица
gender = ''  # Пол
weight = 0.0  # Вес
is_legal = ''  # Признак подозрения в екстремисткой деятельности
contact_phone = ''  # Контактный номер телефона
is_valid = False  # Признак корректности ввода данных

# --------------------------
print('Введите имя лица')
name = input()
while not is_valid:
    if name.find(' ') > 0:
        is_valid = True
    else:
        print('Пожалуйста введите полное имя лица, состоящее минимум из двух слов')
        name = input()
# --------------------------
print('Введите возвраст')
is_valid = False
while not is_valid:
    age = input()
    if age.isdigit():
        if int(age) >= 0:
            is_valid = True
            age = int(age)
    if not is_valid:
        print('Требуется ввести положительное число полных лет возвраста лица')

# --------------------------
print('Введите вес лица')
is_valid = False
while not is_valid:
    weight = input()
    is_valid = True  # Проверка на float выходит за рамки задания
    if not is_valid:
        print('Требуется ввести положительное число в кг')
# --------------------------

print('Введите пол лица М/Ж')
gender = input()
is_valid = False
while not is_valid:
    if gender.upper() == 'М' or gender.upper() == 'Ж':
        is_valid = True
        if gender == 'М' or gender == 'м':
            gender = 'Мужской'
        else:
            gender = 'Женский'
    else:
        print('Введите М или Ж')
        gender = input()

# --------------------------
print('Введите контактный телефон:')
print('+', end=''),
is_valid = False
while not is_valid:
    contact_phone = input()
    if contact_phone.isdigit() and len(contact_phone) >= 11:
        is_valid = True
    else:
        print('Введите полный номер телефона в с кодом страны ')
        print('+', end=''),

# --------------------------
print('Подозревается ли лицо в экстремисткой деятельности? (Да/Нет)')
is_valid = False
is_legal = input()
while not is_valid:
    if is_legal.upper() == 'ДА' or is_legal.upper() == 'НЕТ' or is_legal.upper() == 'Н' or is_legal.upper() == 'Д':
        is_valid = True
        if is_legal.upper() == 'ДА' or is_legal.upper() == 'Д':
            is_legal = 'Подозревается в экстремисткой деятельности'
        else:
            is_legal = 'В противозакооной активности не замечен'
    else:
        print('Введите Да или Нет')
        is_legal = input()

# ------------------------------
print('Данные по нашему лицу:\n', f'Имя: {name}\n', f'Возвраст: {age} лет\n', f'Вес: {weight} кг\n',
      f'Пол: {gender.upper()}\n',
      f'Контактный номер: +{contact_phone}\n', f'Статус лица: {is_legal}')

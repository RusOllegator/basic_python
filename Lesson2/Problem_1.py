# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.


list = [1, '1', '1.0', complex(5, 6), True, 'Какая-то надпись', ['А тут будет список', ['А в нем еще один', 4]],
        tuple('А тут будет кортедж'), ('и', 'еще', '1'),
        set('добавим 1но множество'), {'Ключ 1': 'Словарь', 'Ключ 2': 'То же нужен', 5: 4}, None]

i = 0
for n in list:
    i += 1
    print(f'Тип данных {i}го элемента массива: {type(n)}')

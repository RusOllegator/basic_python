# Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
goods = []

while True:
    print('Выедите идентификатор товара (0 - выход): ', end='')
    article = input()
    print('Выедите название товара: ', end='')
    name = input()
    print('Выедите цену товара: ', end='')
    price = input()
    print('Выедите количество товара на складе: ', end='')
    count = input()
    print('Выедите единицу измерения товара: ', end='')
    metric = input()
    goods.append((article, {'Название': name, 'Цена': price, 'Количество': count, 'ед': metric}))

    #   Запрос на продолжение работы
    print('Ввести реквизиты следующего задания? (Да/Нет):', end='')
    out = False
    while True:
        is_continue = input()
        if is_continue.upper() == 'ДА' or is_continue.upper() == 'Д':
            break
        elif is_continue.upper() == 'НЕТ' or is_continue.upper() == 'Н':
            out = True
            break
        else:
            print('Введите Да или Нет: ', end='')

    if out:
        break

print(f'Наша струткура: {goods}')

# Делаем аналитику
goods_dict = {}
goods_name = set()
goods_price = set()
goods_count = set()
goods_metric = set()

for i in goods:
    goods_name.add(i[1].get('Название'))
    goods_price.add(i[1].get('Цена'))
    goods_count.add(i[1].get('Количество'))
    goods_metric.add(i[1].get('ед'))

print(goods_name)

goods_dict = {'название': goods_name, 'цена': goods_price, 'количество': goods_count, 'ед': goods_metric}
print('Аналитика по складу:')

print(goods_dict)

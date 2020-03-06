# Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
from random import randrange

init_list_len = randrange(10,20) # Длина исходного списка
init_list = [randrange(-100,100) for i in range(init_list_len)] # Генерируем исходный список

print(f'Исходный список:\n{init_list}')

calculate_list = [i[1] for i in enumerate(init_list[1:]) if i[1] > init_list[i[0]]]

print(f'Расчитанный по заданию список:\n{calculate_list}')

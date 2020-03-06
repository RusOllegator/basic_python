# Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке. Для выполнения задания обязательно использовать генератор.
from random import randrange

init_list_len = randrange(10, 20)  # Длина исходного списка
init_list = [randrange(-5, 5) for i in range(init_list_len)]  # Генерируем исходный список
print(f'Исходный список:\n{init_list}')

calculate_list = [i for i in init_list if init_list.count(i) == 1]
print(f'Расчитанный по заданию список:\n{calculate_list}')

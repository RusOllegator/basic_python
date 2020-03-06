# Реализовать два небольших скрипта:
# а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
# б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
from sys import argv
from itertools import count, cycle

init_digit = int(argv[1])  # генерируем числа начиная c заданного
count_digit = int(argv[2])  # количество элементов генерируемого списка
count_repeat = int(argv[3])  # Количесвто элементов списка второго задания


def generate_list(init_dig: int, limit=10):
    ret = []
    for i in enumerate(count(init_dig)):
        if i[0] > limit:
            break
        else:
            ret.append(i[1])
    return ret


def cycle_list(input_list: list, count_repeat: int):
    ret = []
    for i in enumerate(cycle(input_list)):
        if i[0] > count_repeat:
            break
        ret.append(i[1])
    return ret


print(f'Первый список:\n{generate_list(init_digit, count_digit)}')
print(f'Второй список:\n{cycle_list(generate_list(init_digit, count_digit), count_repeat)}')

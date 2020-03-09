# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
from random import random, randint

# Создаем файл и заполняем сучайными числами через пробел
with open('Lesson5.txt', 'w') as f_digits:
    f_digits.write(''.join([f'{random() * 200 - 100:.3f} ' for i in range(randint(10, 20))]))

# Открываем файл, преобразуем модержимое в список чисел
with open('Lesson5.txt', 'r') as f_digits:
    l_digits = [float(i) for i in f_digits.readline().split()]

print(f'Сумма чисел в нашем сгененрированном файле: {sum(l_digits)}')

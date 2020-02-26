# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.

print('Вводите натуральные числа, для выхода из программы введите "exit":',end='')

natural_list = []
while True:
    n = input()
    if not n.isdigit() and n.lower() != 'exit':
        print('Натуральное число, это целое положительное число (1,2,3 ...)')
    elif n.lower() == 'exit':
        break
    else:
        if natural_list.count(int(n)) > 0:
            natural_list.insert(natural_list.index(int(n))+natural_list.count(int(n)),int(n))
        else:
            natural_list.append(int(n))
            natural_list.sort(reverse=True)
    print(f'Текущая структура: {natural_list}')
    print('Введите следующее число (exit - Выход): ',end='')


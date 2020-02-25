#Problem: Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369

print('Введите целое число n: ', end='')
is_valid = False  # Признак корректности ввода данных

while not is_valid:
    n = input()
    if n.isdigit():
        is_valid = True
    else:
        print('Требуется ввести целое число')

print('Найдем n + nn + nnn:\n', f'{n} + {n*2} + {n*3} = {int(n)+int(n*2)+ int(n*3)}')

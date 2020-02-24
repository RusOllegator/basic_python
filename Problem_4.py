# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.

print('Введите целое число n: ', end='')
is_valid = False  # Признак корректности ввода данных
while not is_valid:
    n = input()
    if n.isdigit() and n != '0':
        is_valid = True
        n = int(n)
    else:
        print('Требуется ввести целое положительное число')

current_max_digit = n % 10;
current_number = n // 10;

while current_number > 0:
    current_digit = current_number % 10
    if current_digit > current_max_digit:
        current_max_digit = current_digit
    current_number = current_number // 10

print(f'Вы ввели число: {n}\n', f'Самая большая цифра в вашем числе: {current_max_digit}', sep='')

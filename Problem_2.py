# Problem: Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

print('Введите время в секундах: ', end='')

is_valid = False  # Признак корректности ввода данных

while not is_valid:
    input_sec = input()
    if input_sec.isdigit():
        is_valid = True
        input_sec = int(input_sec)
    else:
        print('Требуется ввести целое число')

calc_h = input_sec // 3600
calc_m = (input_sec - calc_h * 3600) // 60
calc_s = str(input_sec - calc_h * 3600 - calc_m * 60)
calc_h = str(calc_h)
calc_m = str(calc_m)

if len(calc_s) == 1:
    calc_s = '0' + calc_s

if len(calc_m) == 1:
    calc_m = '0' + calc_m

if len(calc_h) == 1:
    calc_h = '0' + calc_h

print(f'Вы ввели время: {input_sec} с\n', f'В формате чч:мм:сс это будет: {calc_h}:{calc_m}:{calc_s}', sep='')

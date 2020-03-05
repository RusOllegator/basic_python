# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
def devide_func(a, b):
    """
    :param a: Вещественное число
    :param b: Вещественное число
    :return: -> a / b
    """
    try:
        return a / b
    except ZeroDivisionError:
        return 'Деление на 0 невозможно'


while True:
    print('Введите значение чеслителя: ', end='')
    a = float(input())
    print('Введите значение знаменателя: ', end='')
    b = float(input())
    print(
        f'Рузкльтат {a}/{b}: {devide_func(a, b)}\n Введите Enter для продолжение, введите exit + enter для выхода из программы\n',
        end='')
    if input() == 'exit':
        break

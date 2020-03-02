# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def my_func(a, b, c):
    """ Возвращает сумму наибольших двух аргументов. """
    return a + b if a >= c and b >= c else a + c if a >= b else b + c


print('Введите через пробел три числа:\na= ', end='')
a = float(input())
print('b= ', end='')
b = float(input())
print('c= ', end='')
c = float(input())

print(f'Сумма наибольших двух ввыеденных чисел: {my_func(a, b, c)}')

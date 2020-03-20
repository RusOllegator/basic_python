# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

class Complex:
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __add__(self, other):
        return Complex(self.re + other.re, self.im + other.im)

    def __mul__(self, other):
        return Complex(self.re * other.re - self.im * other.im, self.re * other.im + self.im * other.re)

    def __str__(self):
        return f"{self.re}{'+' if self.im > 0 else '-' if self.im < 0 else '' }{str(abs(self.im))+'j' if self.im !=0 else ''}"


a = Complex(3,-5)
b = Complex(13,1)
c = Complex(10,0)

print(a+b)
print(a*b)
print(c)
print('-----------------------------------')
# Проверим штатной штукой на корректность:

a1 = complex(3,-5)
b1 = complex(13,1)
c1 = complex(10,0)
print(a1+b1)
print(a1*b1)
print(c)
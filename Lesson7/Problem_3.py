# Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (add()), вычитание (sub()), умножение (mul()), деление (truediv()).
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и обычное (не целочисленное) деление клеток, соответственно.
# В методе деления должно осуществляться округление значения до целого числа.
from math import trunc


class Cell:
    def __init__(self, init_unit: int):
        self.unit = init_unit

    @property
    def unit(self):
        return self.__unit

    @unit.setter
    def unit(self, new_unit):
        self.__unit = abs(trunc(new_unit))

    def __add__(self, other):
        return Cell(self.__unit + other.__unit)

    def __sub__(self, other):
        if self.__unit >= other.__unit:
            return Cell(self.__unit - other.__unit)
        else:
            print('Операция невозможна')
            return 0

    def __mul__(self, other):
        return Cell(self.__unit * other.__unit)

    def __truediv__(self, other):
        return Cell(trunc(self.__unit / other.__unit))

    def make_order(self, untit_in_row):
        string = ''
        n = self.__unit  # остаток клеток
        while n > 0:
            for i in range(untit_in_row):
                string += '*'
                n -= 1
                if n == 0:
                    break
            string += '\n'
        return string[:-1]


cell_1 = Cell(20)
cell_2 = Cell(8)
cell_3 = Cell(-5.5)
cell_4 = cell_1 / cell_3

print((cell_1 - cell_2).make_order(3))
print('------------------------------')

print(cell_4.make_order(2))
print('------------------------------')

print((cell_3 * cell_4).make_order(5))
print('------------------------------')

print(cell_2 - cell_1)

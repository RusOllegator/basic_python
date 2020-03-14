# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
from abc import ABC, abstractmethod, abstractproperty


class Clothes(ABC):
    def __init__(self, gender_type):
        self.gender_type = gender_type

    @abstractmethod
    def cloth_metric(self):
        pass

    @abstractmethod
    def material_debit(self):
        pass

    @abstractmethod
    def debit_formula(self):
        return None

    @abstractmethod
    def gender_type(self):
        pass


class Coat(Clothes):
    def __init__(self, size, gender_type):
        self.__size = size
        super().__init__(gender_type)

    @property
    def cloth_metric(self):
        return self.__size

    @property
    def material_debit(self):
        return self.debit_formula()

    def debit_formula(self):
        return f'{self.__size / 6.5 + 0.5: .2f}'

    @property
    def gender_type(self):
        return self.__gender_type

    @gender_type.setter
    def gender_type(self, gender_type):
        if gender_type.upper() in ['M', 'MAN', 'М', 'МУЖ']:
            self.__gender_type = 'man'
        elif gender_type.upper() in ['W', 'WOMEN', 'Ж', 'ЖЕН']:
            self.__gender_type = 'women'
        else:
            self.__gender_type = 'unisex'


class Costume(Clothes):
    def __init__(self, height, gender_type='unisex'):
        self.__height = height
        super().__init__(gender_type)

    @property
    def cloth_metric(self):
        return self.__height

    @property
    def material_debit(self):
        return self.debit_formula()

    def debit_formula(self):
        return self.__height * 2 + 0.3

    @property
    def gender_type(self):
        return self.__gender_type

    @gender_type.setter
    def gender_type(self, gender_type):
        if gender_type.upper() in ['M', 'MAN', 'М', 'МУЖ']:
            self.__gender_type = 'man'
        elif gender_type.upper() in ['W', 'WOMEN', 'Ж', 'ЖЕН']:
            self.__gender_type = 'women'
        else:
            self.__gender_type = 'unisex'


armani = Coat(30, 'Ж')
print(armani.gender_type)
print(armani.cloth_metric)
print(armani.material_debit)
print('***********************')

brioni = Costume(40)
print(brioni.gender_type)
print(brioni.cloth_metric)
print(brioni.material_debit)
print('***********************')

gucci = Costume(30, 'детский')
print(gucci.gender_type)
print(gucci.cloth_metric)
print(gucci.material_debit)

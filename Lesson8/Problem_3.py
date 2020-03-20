# Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.

class MyList:
    print_list = []

    # Попробуем сделать исключение как класс в классе..
    @staticmethod
    class NotFloatExcept(Exception):
        def __init__(self, txt):
            self.txt = txt

    # Проверим что вновь введенная строка является числом, если да, перобразуем к числовому типу
    def __is_float(self, input_str):
        is_one_dot, is_one_minus = 0, 0
        for i in input_str:
            if ord(i) >= 48 and ord(i) <= 57:
                pass
            # В числе может быть одн точка
            elif ord(i) == 46 and is_one_dot == 0:
                is_one_dot += 1
            # А еще минус
            elif ord(i) == 45 and is_one_minus == 0:
                is_one_minus += 1
            else:
                raise self.NotFloatExcept('Введенная строка не является числом!')

        #  Если число целое, так и вернем
        if is_one_dot == 0:
            return int(input_str)
        return float(input_str)

    # Добавляем новое число в список
    def __call__(self, new_str):
        try:
            self.print_list.append(self.__is_float(new_str))
        except self.NotFloatExcept as e:
            print(e)

    # Выводим на печать
    def __str__(self):

        return str(self.print_list)[1:-1]


list = MyList()

while True:
    print('Введите число: ', end='')
    n = input()
    if n == '':
        print('Окончание программы')
        break
    else:
        list(n)
        print(list)

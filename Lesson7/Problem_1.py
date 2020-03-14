# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()), который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    """
    Класс матрица, при инициализации следует передать список, состоящий из списков
    Пустые ячейки заполняются нулями.
    Атрибуты:
    _is_init определяет кооректность инициализации класса
    __matrix_size кортедж из двух значений, определяющий размер матрицы
    matrix матрица
    """
    _is_init = False

    def __init__(self, matrix):
        if self.__is_init_f(matrix):
            self.matrix = self.__fill_matrix(matrix)
        else:
            self.__matrix_size_f(matrix)

    # Метод проверяет, что нам передали список списков при инициализации
    def __is_init_f(self, matrix):
        if isinstance(matrix, list):
            for i in matrix:
                if not isinstance(i, list):
                    print('Не удалось инициализировать объект')
                    return False
            self._is_init = True
            return True

    # Метод определяет размер матрицы, если объект класса инициализировался
    def __matrix_size_f(self, matrix):
        if not self._is_init:
            self.matrix_size = (0, 0)
        else:
            n_row = len(matrix)
            max_col = 0
            for i in matrix:
                if len(i) > max_col:
                    max_col = len(i)
            self.matrix_size = (n_row, max_col)

    # Функция заполнит недостающие ячейки матрицы нулями
    def __fill_matrix(self, matrix):
        self.__matrix_size_f(matrix)
        size = self.matrix_size
        for row in range(size[0]):
            for col in range(len(matrix[row]), size[1]):
                matrix[row].append(0)
        return matrix

    # Отображение нашей матрицы
    def __str__(self):
        str_matix = ''
        for r in range(self.matrix_size[0]):
            for c in range(self.matrix_size[1]):
                try:
                    str_matix += str(self.matrix[r][c]) + ' '
                except:
                    str_matix += str(type(self.matrix[r][c])) + ' '
            str_matix += '\n'
        return str_matix

    # Метод расширяет матрицу до требуемого размера new_size
    def fill_to_size(self, new_size):

        for i in range(self.matrix_size[0], new_size[0]):  # заполним новые строки нолями
            self.matrix.append([0 for n in range(self.matrix_size[1])])

        # Зададим новое количество строк нашей матрице
        self.matrix_size = (max(self.matrix_size[0], new_size[0]), self.matrix_size[1])

        for i in range(self.matrix_size[1], new_size[1]):  # Заполним новые стобцы нолями
            for row in range(self.matrix_size[0]):
                self.matrix[row].append(0)

        # Зададим новое количество столбцов гашей матрице
        self.matrix_size = (self.matrix_size[0], max(self.matrix_size[1], new_size[1]))

    # Реализуем сложение матриц друг сдругом
    def __add__(self, other):
        # Приведем матрицы к одному размеру
        self.fill_to_size(
            (max(self.matrix_size[0], other.matrix_size[0]), max(self.matrix_size[1], other.matrix_size[1])))
        other.fill_to_size(
            (max(self.matrix_size[0], other.matrix_size[0]), max(self.matrix_size[1], other.matrix_size[1])))

        new_matrix = [[self.matrix[row][col] + other.matrix[row][col] for col in range(self.matrix_size[1])] for row in
                      range(self.matrix_size[0])]

        return Matrix(new_matrix)


item_1 = Matrix([[1, 2], [3, 4], [5, 6, 7]])
item_2 = Matrix([[6, 7], [8, 9, 100], [5, 6, 7], [10, 20, 30, 40], [], [-4, 3, 2, 0]])

a = Matrix(1)

print(f'Первая матрица: ')
print(item_1)

print(f'Вторя матрица: ')
print(item_2)

print(f'Сумма матриц: ')
print(item_1 + item_2)


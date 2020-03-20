# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

# Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.

# Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.

from abc import ABC, abstractmethod


class MyStorage:
    """
    Склад будет описываться количеством места под технику, в виде трехмерной матрицы:
    [row] - номер ряда
    [col] номер в ряду
    [flor] - номер "этажа" на стелаже
    [size] - размер конкртеной ячейки

    Будет обладать интерфейсными методами:
    get_item - выдать единицу товара
    put_item - принять на хранение единицу товара
    check_get - проверить возможность выдать товар со склада
    check_put - проверить возможность поместить товар на склад
    get_item_count - возвращает количество товаров данного класса

    Внутренними методами:

    Каждый помещенный на склад товар обладает уникальным инвентарным номером invent_number
    и артикулом, характеризующем тип товара
    Находящиесть на складе товары вносятся в справочник goods_dict, ключем которого является артикул товара,
    а значение список, состоящий из инвентарных номеров:
    Справочник goods_size_param_dict хранит размер единицы товара соответсвующего артикула
    Справочник inventory_dict соотносит инвентарный номер товара с его местом на складе
    Справочник goods_type  соотносит артикул с типом и названием товара

    """

    goods_dict = {}
    goods_size_param_dict = {}
    inventory_dict = {}
    goods_type = {}
    __invent_number_seq = 1000  # Последовательность инвентарных номероа

    def __init__(self, storage_size):
        self.storage_size = storage_size

    def check_get(self, articul_number=None, invent_number=None):
        """Функция проверяет возможность выдать указанный товар со склада"""
        if articul_number is not None and invent_number is not None:
            raise self.ItemNotDefine
        elif invent_number is not None:
            try:
                try:
                    self.inventory_dict[invent_number]
                    self.__seech_item_by_ivent(invent_number)
                except KeyError:
                    raise self.ItemNotFound
            except self.ItemNotFound as e:
                return False, e.txt
            else:
                return True, None
        elif articul_number is not None:
            try:
                try:
                    self.goods_type[articul_number][0]
                except IndexError:
                    raise self.ItemNotFound
                except KeyError:
                    raise self.ItemNotFound
            except self.ItemNotFound as e:
                return False, e.txt
            else:
                return True, None
        else:
            raise self.ItemNotDefine

    # Выдача товара, по инвентарному номеру - конкретного экземляра, или по артикулу - первый этого типа
    def get_item(self, articul_number=None, invent_number=None):
        try:
            is_check, msg = self.check_get(articul_number=articul_number, invent_number=invent_number)
        except self.ItemNotDefine as e:
            return e.txt
        except self.ItemNotFound as e2:
            return e2.txt

        if is_check:
            if invent_number is not None:

                place = self.inventory_dict.pop(invent_number)
                articul_number = self.__seech_item_by_ivent(invent_number)

                # Добавляем место в ячейке на складе
                self.storage_size[place[0]][place[1]][place[2]] += self.goods_size_param_dict[articul_number]
                # удаляем из справочника товаров
                self.goods_dict[articul_number].remove(invent_number)
                return f"Товар {self.goods_type[articul_number][1]} c инвентарным номером {invent_number} выдан со склада"
            else:
                invent_number = self.goods_dict[articul_number][0]
                place = self.inventory_dict.pop(invent_number)
                self.storage_size[place[0]][place[1]][place[2]] += self.goods_size_param_dict[articul_number]
                self.goods_dict[articul_number].remove(invent_number)
                return f"Товар {self.goods_type[articul_number][1]} c инвентарным номером {invent_number} выдан со склада"
        else:
            return msg

    def __seech_item_by_ivent(self, invent_number):
        """Поиск артикула товара по его инвентарному номеру"""
        for i in self.goods_dict:
            if invent_number in self.goods_dict[i]:
                return i
        raise self.ItemNotFound

    def put_item(self, goods_item):
        """Функция принимает на склад товар"""
        is_check, msg = self.check_put(goods_item.size)
        if is_check:
            item_place = self.__find_cell(goods_item.size)
            self.__invent_number_seq += 1  # Дадим новый инвентарный номер товару
            self.inventory_dict.setdefault(self.__invent_number_seq, item_place)

            # Запишем в справочники новый товар на складе
            if self.goods_size_param_dict.get(goods_item.articul) is None:
                self.goods_size_param_dict[goods_item.articul] = goods_item.size

            if self.goods_dict.get(goods_item.articul) is None:
                self.goods_dict[goods_item.articul] = [self.__invent_number_seq]
            else:
                self.goods_dict[goods_item.articul].append(self.__invent_number_seq)

            if self.goods_type.get(goods_item.articul) is None:
                self.goods_type[goods_item.articul] = (goods_item.type, goods_item.name)

            # Уменьшим размер ячейки хранения на занятый
            self.storage_size[item_place[0]][item_place[1]][item_place[2]] -= goods_item.size
            return 'Товар принят на склад', self.__invent_number_seq
        else:
            return 'Товар не возможно принять на склад:\n' + msg, None

    # Функция проверяет может ли склад принять товар
    def check_put(self, size):
        try:
            self.__find_cell(size)
        except self.NotEnoughSpace as E:
            return False, E.txt
        else:
            return True, None

    def __find_cell(self, size):
        """Ищем номер первой ячейки, в которм места больше переданного параметра"""
        for x in range(len(self.storage_size)):
            for y in range(len(self.storage_size[x])):
                for z in range(len(self.storage_size[x][y])):
                    if self.storage_size[x][y][z] >= size:
                        return x, y, z
        raise NotEnoughSpace

    def get_item_count(self, goods_item):
        """Функция вернет количестов товаров на складе указанного типа"""
        try:
            return len(self.goods_dict[goods_item.articul])
        except:
            return 0

    # Тут будет блок всяких исключений
    class NotEnoughSpace(Exception):
        def __init__(self):
            self.txt = 'Не достаточно места на складе!'

    class NotGettingGoods(Exception):
        def __init__(self):
            self.txt = 'Не вохможно выдать указанный товар'

    @staticmethod
    class ItemNotFound(Exception):
        def __init__(self):
            self.txt = 'Товара нет на складе!'

    class ItemNotDefine(Exception):
        def __init__(self):
            self.txt = 'По входным данным невозможно понять, что за товар!'


class Orgtekhnika(ABC):
    def __init__(self, type, name, size, articul, price):
        self.type = type
        self.name = name
        self.size = size
        self.articul = articul
        self.price = price


class Printer(Orgtekhnika):
    def __init__(self, name, size, articul, price, speed, print_type):
        super().__init__('Принтер', name, size, articul, price)
        self.print_type = print_type
        self.speed = speed


class Scanner(Orgtekhnika):
    def __init__(self, name, size, articul, price, dpi, scanner_type):
        super().__init__('Сканер', name, articul, size, price)
        self.dpi = dpi
        self.scanner_type = scanner_type


class Kserox(Orgtekhnika):
    def __init__(self, name, size, articul, price, speed, kserox_type, is_color):
        super().__init__('Ксерокс', name, articul, size, price)
        self.speed = speed
        self.is_color = is_color
        self.kserox_type = kserox_type

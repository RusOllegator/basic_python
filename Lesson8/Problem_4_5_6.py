# Проверка реализованных классов для заданий 4 5 и 6

from Problem_4_5_6_classes import *

# Размер склада
storage_size = [[[50, 30, 30], [50, 30, 30], [50, 30, 30]],
                [[50, 30, 30], [50, 30, 30], [50, 30, 30], [40, 40]],
                [[50, 30, 30], [50, 30, 30], [50, 30, 30], [100]]]

my_storage = MyStorage(storage_size)

# Проверяем получение товара по не правильным реквизитам
print(my_storage.get_item(articul_number=2134321))
print(my_storage.get_item())
print('------------------------------------------------')
my_print_1 = Printer(name='HP LaserJet 1000 pro', size=20, articul=2134321, price=1154.32, speed=8, print_type='Laser')

# Положим три принтера на склад
print(my_storage.put_item(my_print_1))
print(my_storage.put_item(my_print_1))
print(my_storage.put_item(my_print_1))

# Один из них заберем
print(my_storage.get_item(my_print_1.articul))
# Попробуем по инвентарному номеру
print(my_storage.get_item(invent_number=1001))
# По другому
print(my_storage.get_item(invent_number=1002))

# Посмотрм сколько останется
print(my_storage.get_item_count(my_print_1))

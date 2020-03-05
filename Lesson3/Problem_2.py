# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

def print_identification(name, second_name, year_of_birth, city, mail, phone):
    """ Выводит в строку данные пользователя """
    print(f'Данные пользователя:\n{name} {second_name} {year_of_birth} года рождения ' \
          f'проживающий в {city}, e-mail: {mail}, Tel.: {phone}')


print_identification(name='Олег', second_name='ТАкой-то', year_of_birth=1985, city='Урюпинск', mail='oleg@mail.ru',
                     phone='+79001234567')

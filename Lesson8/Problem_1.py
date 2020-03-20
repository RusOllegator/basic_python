# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class Date:
    def __init__(self, str_date):
        self.str_date = str_date

    @classmethod
    def extract_date(cls, str_date: str):
        l_date = [item for item in str_date.split('-')]
        # возможно использовался сокращенное написание года
        if len(l_date[2]) == 2:
            l_date[2] = '20' + l_date[2]
        try:
            l_date = [int(item) for item in l_date]
            return cls.date_validation(l_date[0], l_date[1], l_date[2])
        except Exception as e:
            return 'Дата передана в неверном формате' + '\n' + str(e)

    @staticmethod
    def date_validation(dd, mm, yyyy):

        # справочник количества дней в месяце
        days_in_month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
                         7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        # Проверим год на "високостность", изменим справочник если эта проверка пройдет
        if (yyyy % 4 == 0) or (yyyy % 100 == 0 and yyyy % 400 != 0):
            days_in_month[2] = 29

        if not (yyyy > 0 and yyyy < 2999):  # считааем окончание тысячителетия концом эпохи
            return 'Дата передана в неверном формате'

        if not (mm > 0 and mm < 13):
            return 'Дата передана в неверном формате'

        if not (dd > 0 and dd <= days_in_month[mm]):
            return 'Дата передана в неверном формате'

        return 'Дата передана в верном формате'

    def print_date_condition(self):
        print(Date.extract_date(self.str_date), '\n-----------------')


date_1 = Date('14-12-0004')
date_2 = Date('29-02-2020')
date_3 = Date('10-10-20')
date_4 = Date('29-02-2019')
date_5 = Date('24-02-189')

date_1.print_date_condition()
date_2.print_date_condition()
date_3.print_date_condition()
date_4.print_date_condition()
date_5.print_date_condition()

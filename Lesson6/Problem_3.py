# Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker. В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    _income = {'Разнорабочий': {"wage": 1000, "bonus": 200}, 'Одннообразный рабочий': {"wage": 800, "bonus": 100},
               'Погонщик рабочих': {"wage": 3000, "bonus": 1000},
               'Во всем виноватый инженегр': {"wage": 400, "bonus": 100}}
    position = ''

    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname


class Position(Worker):
    def __init__(self, name, surname, position: str):
        self.position = position
        super().__init__(name, surname)

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        if self.position in self._income.keys():
            return self._income[self.position]["wage"] + self._income[self.position]["bonus"]
        else:
            'В табель не внесены данные о доходе на данной позиции'


slave = Position(name='Иван', surname='Иванов', position='Разнорабочий')

print(slave.position)
print(f'Имя рабочего: {slave.get_full_name()}')
print(f'Доход за месяц: {slave.get_total_income()}')

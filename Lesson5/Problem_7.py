# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
from my_func import didgits_of_string  # Воспользуемся готовой ф-ией из предыдущего задания - не получилось
from json import dump

# Создаем список из строк файла
with open('Problem_7.txt', 'r') as f_objects:
    l_objects = f_objects.readlines()

d_firms = {}  # Справочник названий фирм с их прыбылью
for firm in l_objects:
    income, charges = didgits_of_string(firm)
    d_firms[firm.split()[0]] = income - charges
    profit, i = 0, 0
    if income - charges > 0:
        i += 1
        profit += income - charges
l_result = []
l_result.append(d_firms)

# Подсчет средней прибыли. Включая случай, чо все компании убыточны
try:
    avg_profit = profit / i
except ZeroDivisionError:
    avg_profit = 'NaN'

l_result.append({"average_profit": avg_profit})

with open('Problem_7.json', 'w') as f_json:
    dump(l_result, f_json)

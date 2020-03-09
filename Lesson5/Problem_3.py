# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

f_persons = open('Problem_3.txt', 'r')
persons_raw = f_persons.readlines()
f_persons.close()

work_tab = {}  # Справочник зарплат
f_averege = lambda x: sum(x) / len(x)  # Функция подсета среднего значения
f_smaller = lambda x, y: True if x < y else False  # Функция фозвращает True, если первый аргумент меньше второго

# Заполнили справочник
for item in persons_raw:
    work_tab[item.split(' ')[0]] = int(item.split(' ')[1][0:-1])
print('Сотрудники имеющие оклад меньше 20000 тугриков:')

for i in work_tab:
    if f_smaller(work_tab.get(i), 20000):
        print(i)

print(f'Средняя вличина зарплат сотрудников: {f_averege(work_tab.values())} тугриков')

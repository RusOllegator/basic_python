# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.
my_file = open('Problem_2.txt', 'r')
for i, line in enumerate(my_file):
    print(f'Количество слов в {i + 1}ой строке:{len(line.split(" "))}')
print(f'Количество строк в файле: {i + 1}')
my_file.close()

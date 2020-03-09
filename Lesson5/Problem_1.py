# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

print(f"Введите имя фала, куда осуществится запись: ", end='')
filename = input()
my_file = open(filename, 'w')
print(f"Вводите строки, для записи в файл, для окончания введите пустую строку")
while True:
    input_string = input()
    if input_string == '':
        my_file.close()
        break
    my_file.write(input_string)

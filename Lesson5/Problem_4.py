# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

# Справочник соответсвия русских и английских наименований цифр
dict_digit = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре", "Five": "Пять",
              "Six": "Шесть", "Seven": "Семь", "Eight": "Восемь", "Nine": "Девять", "Zero": "Ноль"}

with open("Problem_4.txt", "r") as f_digits:
    l_digits = f_digits.readlines()

# Запишем результат, подменив первое слово значением из словаря
with open("Problem4_result.txt", 'w') as f_reuslt:
    for i in l_digits:
        f_reuslt.write(i.replace(i[:i.index(' ')], dict_digit[i[:i.index(' ')]]))

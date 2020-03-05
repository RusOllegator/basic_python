# Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

def sum_string(current_sum, input_list):
    """

    :param current_sum: foat
    :param input_list: list of float
    :return: float + sum(input_list)
    """
    numirate_list = []
    for i in input_list:
        try:
            numirate_list.append(float(i))
        except ValueError:
            if i == 'exit':
                return current_sum + sum(numirate_list), False
    return sum(numirate_list) + current_sum, True


flag = True  # Признак завершения ввода чисел
current_sum = 0

while flag:
    print('Вводите через пробел числа. Для заверщения введите exit')
    L = input().split(' ')
    current_sum, flag = sum_string(current_sum, L)
    print(f'Сумма введенных чисел: {current_sum}')

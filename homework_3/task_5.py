# 5) Программа запрашивает у пользователя строку чисел,разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить
# ввод чисел,разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ,выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале
# нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

def number_sum(*args):

    """Подсчёт суммы вводимых пользователем чисел

    Логика работы функции:
    1.получить строку чисел, разделенных пробелом от пользователя; тип данных - str
    2.создать из строки список с помощью метода split(); тип данных - list
    3.привеси элементы списка list_user_num к типу int,
    записывая результат в список list_user_num
    4.расчитать сумму элементов списка
    5.в бесконечном цикле предлагать пользователю остановить программу
    или продлжить работу
    6.если пользователь продолжает программу, добавлять новые введеные числа
    к сумме списка list_user_num
    7.при введении спецсимвола 'q' после нескольких чисел, добавлять числа, введеные до
    спецсимвола к общей сумме и затем прекращать работу программы
    8.выход из программы осуществляется путем ввода спецсимвола 'q'

    Переменные:
    user_num - первоначалный набор данных от пользователя; тип данных - str
    list_user_num - список, преобразованный из user_num; тип данных - list
    common_sum - результат суммирования элементов из списка list_user_num; тип данных - int
    user_act -  набор данных от пользователя, получаемый после первой иттерации; тип данных - str
    user_act - список, преобразованный из user_act; тип данных - list

    """

    user_num = input('Enter a few number through the spacebar: ')
    list_user_num = user_num.split()
    list_user_num = [int(i) for i in list_user_num]
    common_sum = sum(list_user_num)
    print(common_sum)
    while True:
        user_act = input('Press q to exit the program.''To continue working,\n'
                         'enter a few number through the spacebar:  ', )
        if user_act == 'q':
            print('END')
            break
        else:
            user_act = user_act.split()
            if 'q' in user_act:
                n = user_act.index('q')
                user_act = user_act[:n]
                user_act = [int(i) for i in user_act]
                list_user_num.extend(user_act)
                common_sum = sum(list_user_num)
                print(common_sum)
                print('END')
                break
            else:
                user_act = [int(i) for i in user_act]
                list_user_num.extend(user_act)
                common_sum = sum(list_user_num)
                print(common_sum)













number_sum()
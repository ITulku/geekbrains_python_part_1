# 6) Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля ​itertools​.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3,
# а при достижении числа 10 завершаем цикл. Во втором также необходимо
# предусмотреть условие, при котором повторение элементов списка будет прекращено

import itertools
def love_func():
    """Возвращает указанное количество повторений элементов списка"""
    work_list = ['Л','Ю','Б']
    result_list = []
    while True:
        try:
            end_val = int(input('Enter the required number of variants: '))
            count = 0
            for i in itertools.cycle(work_list):
                if count > end_val:
                    break
                else:
                    result_list.append(i)
                    count += 1
            result = ''.join(result_list)
            return result
        except ValueError:
            print('Enter only numerical values!')

print(love_func())



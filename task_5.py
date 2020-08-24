# 5) Реализовать формирование списка, используя функцию range()
# и возможности генератора. В список должны войти четные числа
# от 100 до 1000 (включая границы). Необходимо получить
# результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию ​reduce().
import functools

def count_func(a,b):
    """Произведение всех чётных чисел в заданном диапозоне"""
    work_list = [el for el in range(a,b+1) if el % 2 == 0 ]
    result = functools.reduce(lambda x,y: x * y, work_list)
    return result



print(count_func(2,10))
print(count_func(100,1000))




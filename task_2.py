# 2. Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().


source_list = list(input('Enter a number:'))
# print(source_list)

n = 0
for i in range(int(len(source_list) / 2)):
    source_list[n], source_list[n + 1] = source_list[n + 1], source_list[n]
    n += 2


print(source_list)
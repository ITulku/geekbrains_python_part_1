# 5. Реализовать структуру «Рейтинг», представляющую
# собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, _3_, 2.
# Пользователь ввел число 8. Результат: _8_, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, _1_.
# Набор натуральных чисел можно задать непосредственно в коде,
# например, my_list = [7, 5, 3, 3, 2].
# - изменять тип добавляемого значения для наглядности
# - не использовать .reverse(), .sort()


my_list = [99,70,43,43,43,21,17,17,9,3]

new_number = int(input('Enter a number: '))

# if new_number > my_list[0]:
#     my_list.insert(0, str(new_number))
# if new_number < my_list[-1]:
#     my_list.append(str(new_number))
#
# for i in range(int(len(my_list))):
#     if new_number == my_list[i]:
#         j = my_list.count(my_list[i])
#         if j > 1:
#             my_list.insert((i + j), str(new_number))
#             break
#
#
#
# print(my_list)

i = 0
for n in my_list:
    if new_number <= n:
        i += 1
my_list.insert(i,str(new_number))

print(my_list)

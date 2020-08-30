# 3. Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

### числа от 1 до 9 ###
# user_number = int(input('Enter a number: '))
# double_number = user_number * 11
# triple_number = user_number * 111
# numbers_sum = user_number + double_number + triple_number
#
# print(numbers_sum)

### любые целые числа ###
user_number = input('Enter a number: ')# не переводим в int, чтобы можно было сделать конкатенацию
# if user_number < '0':
#     print('Enter positive integer')
#     user_number = input('Enter a number: ') надо дописать проверку

double_number = int(user_number + user_number) # конкатенируем и приводим к int
triple_number = int(user_number + user_number + user_number) # конкатенируем и приводим к int
numbers_sum = int(user_number) + double_number + triple_number # складываем, приводя user_number к int

print(int(user_number),f'+ {double_number} + {triple_number} = {numbers_sum}')

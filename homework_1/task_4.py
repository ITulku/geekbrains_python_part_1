# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

user_number = int(input('Enter a positive integer: '))
max_number = user_number % 10 # получаем последнюю цифру из числа ; считаем, что последняя цифра - самая большая
user_number = user_number // 10 # убираем учтённую последюю цифру из числа

while user_number > 0: # до тех пор, пока число имеет больше 0 цифр
    if user_number % 10 > max_number: # если последняя цифра числа больше текущего max_number
        max_number = user_number % 10 # перезаписываем новое значенеие в max_number
    else:
        user_number = user_number // 10 # иначе отбрасываем следубщую последнюю цифру
print(f'The biggest numeral is {max_number}')


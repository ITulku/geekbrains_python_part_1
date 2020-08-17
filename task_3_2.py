# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц
# (зима, весна, лето, осень). Напишите решения через list и через dict.

month_number = int(input('Enter month`s number: '))

#### WAY 1 ####
# year_list = ['', 'winter', 'winter', 'spring', 'spring',
#              'spring', 'summer', 'summer', 'summer',
#              'autumn', 'autumn', 'autumn', 'winter'
#              ]
# result = f'This is {year_list[month_number]}`s month.'
# print(result)


#### WAY 2 ####
year_list = ['winter', 'spring', 'summer', 'autumn']
if month_number in range(1,3) or month_number == 12:
    print(f'This is {year_list[0]}`s month.')
if month_number in range(3,6):
    print(f'This is {year_list[1]}`s month.')
if month_number in range(6,9):
    print(f'This is {year_list[2]}`s month.')
if month_number in range(9,12):
    print(f'This is {year_list[3]}`s month.')





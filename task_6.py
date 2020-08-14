# 6. Спортсмен занимается ежедневными пробежками.
# В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
# Например: a = 2, b = 3.
# Результат:
# 1-й день: 2
# 2-й день: 2,2
# 3-й день: 2,42
# 4-й день: 2,66
# 5-й день: 2,93
# 6-й день: 3,22
# Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.

first_result = float(input('Enter first day`s result: '))
goal = float(input('Enter a goal value: '))

day = 1
result = first_result
progress_per_day = (result / 100) * 10 # result * 0.1

while result < goal:
    if result + progress_per_day < goal:
        result = result + progress_per_day
        day += 1
        print(result)
    else:
        day += 1
        print(f'Athlete will reach goal on {day} day.')
        break


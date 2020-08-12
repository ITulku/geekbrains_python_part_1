# 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки
# (соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы
# и определите прибыль фирмы в расчете на одного сотрудника.

proceeds = int(input('Enter the amount of proceeds: '))
costs = int(input('and the amount of costs: '))

if proceeds > costs:
    print('Congratulations! You have a profit!')
    profit = proceeds - costs # в условии не обозначена формула нахождения прибыли.
    # Считем, что прибыль - это разница между выручкой и издержками
    profitability = profit / proceeds
    print(f'Your profitability is {profitability}.')
    employees_number = int(input('How many employees do you have?'))
    profit_per_employee = profit / employees_number
    print(f'Each employee made a profit in {profit_per_employee:.2f}.')

if proceeds < costs:
    print('Wasted! You have a damage...')

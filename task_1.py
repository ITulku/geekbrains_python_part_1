# 1) Реализовать скрипт, в котором должна быть
# предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу:
# (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать
# скрипт с параметрами.

from sys import argv

trash, work_time, rate, prize = argv


salary = (int(work_time) * int(rate)) + int(prize)
print(f'Your salary this month was {salary}. Thanks for your good job!')



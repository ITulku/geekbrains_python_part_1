# 3) Создать текстовый файл (не программно), построчно записать фамилии
# сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 2320 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода
# сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

def min_salary(file):
    """Подсчёт средней зарплаты сотрудников и вывод списка сотрудников с зарплатой, ниже 2320.00"""
    workers = {}
    salary = []
    # min_salary =[]
    low_sal = []
    with open (file) as f:
        for i in f:
            key, value = i.split()
            workers[key] = float(value)
        for val in workers.values():
            salary.append(val)
            mid_sal = round(sum(salary) / len(salary), 2)
        for key in workers.keys():
            if workers[key] < 2320.00:
                low_sal.append(key)
        print(f'Salary less than 2320.00 for employees: {low_sal}.\n'
              f'Average salary is {mid_sal}.' )


min_salary('file_for_task_3.txt')
# 7) Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
# а также среднюю прибыль. Если фирма получила убытки, в расчет средней
# прибыли ее  не включать​
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки, также добавить
# ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000},
# {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1" :  5000 ,  "firm_2" : 3000 , "firm_3":  1000 },
# { "average_profit" :  2000 }]
import re
import json
def companies(file):
    """Создание словаря из данных файла

    Логика работы:
    1.1.открыть файл и начать считывать его построчно
    2.с помощью ркгулярного выражения (шаблон - одна и более цифр подряд) найти в строек
    числа
    3.привести число к типу inr
    4. рассчитать profit фирмы
    5.создать словарь, включающий наименование фирмы, имеющей прибыли и сумму прибыли
    6.создать словарь со значением средней прибыли всех фирм
    7.сохранить словрь с наименованиями фирм и прибылями в формате json

    Переменные:
    profits - значения прибылей фирм; тип данных - list
    comp_dict - наименования фирм и значение их прибылей; тип данных - dict
    aver_dict - средняя прибыль фирм; тип данных - dict
    common_dict - итоговый список: тип данных - list

    """
    profits = []
    comp_dict = {}
    aver_dict = {}
    common_dict = []
    with open(file) as f:
        for i in f:
            content = i.split()
            money = re.findall('\d+',i)
            money = [int(i) for i in money]
            profit = money[0] - money[1]
            key, value = content[0], profit
            comp_dict[key] = value

            if profit > 0:
                profits.append(profit)
    aver_profit = round(sum(profits) / len(profits), 2)
    key, value = 'average_profit', aver_profit
    aver_dict[key] = value

    common_dict.append(comp_dict)
    common_dict.append(aver_dict)
    print(common_dict)

    with open('task_7.json','w') as write_f:
        json.dump(common_dict, write_f)

companies('file_for_task_7.txt')


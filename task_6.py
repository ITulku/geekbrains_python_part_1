# 6. * Реализовать структуру данных «Товары».
# Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно,
# т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
#
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
#
# ]
# Необходимо собрать аналитику о товарах.
# Реализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик,
# например список названий товаров.
# Пример:
# {
#
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
#
# }


products = [] #основной список
num = 1
analyst_dict = {'product`s name':[], 'product`s cost':[],
                'number of product':[], 'product`s units':[]
                } #словарь для аналитики
prod_names = [] #все наименования
prod_costs = [] #все стоимости
prod_numbers = [] #все количества
prod_units = [] #все единицы измерения

user_start_action = input('What would you like to do? Enter the number of the desired action. \n'
         '1. Add a product.\n'
         )
while True:
    if user_start_action == '1':
        prod_name = input('Enter name of product: ')
        prod_cost = input('cost of product: ')
        prod_num = input('number of product: ')
        prod_unit = input('product units: ')
        products.append((num, {'product`s name': prod_name, 'product`s cost': prod_cost,
        'number of product': prod_num, 'product`s  units': prod_unit}))
        num +=1
        prod_names.append(prod_name)
        prod_costs.append(prod_cost)
        prod_numbers.append(prod_num)
        prod_units.append(prod_unit)
        way = input('Do you want to contiune? yes/no ')
        if way == 'yes':
            prod_name = input('Enter name of product: ')
            prod_cost = input('cost of product: ')
            prod_num = input('number of product: ')
            prod_unit = input('product units: ')
            products.append((num, {'product`s name': prod_name, 'product`s cost': prod_cost,
            'number of product': prod_num, 'product`s  units': prod_unit}))
            num +=1
            prod_names.append(prod_name)
            prod_costs.append(prod_cost)
            prod_numbers.append(prod_num)
            prod_units.append(prod_unit)
            way = input('Do you want to contiune? yes/no ')
        if way == 'no':
            user_start_action = input('What would you like to do? Enter the number of the desired action. \n'
         '1. Add a product.\n'
         '2. Show all info.\n'
         '3. Show analyst info\n'                          )
    if user_start_action == '2':
        print(products)

        # for i in products:  # посторочный вывод, но без скобок списка
        #     print(i)

        break
    if user_start_action == '3':
        analyst_dict['product`s name'] = prod_names
        analyst_dict['product`s cost'] = prod_costs
        analyst_dict['number of product'] = prod_numbers
        analyst_dict['product`s units'] = prod_units
        print(analyst_dict) # не знаю, как вывести пары словаря построчно

        # for keys, values in analyst_dict.items(): # посторочный вывод, но без скобок словаря
        #     print(keys, values)

        break


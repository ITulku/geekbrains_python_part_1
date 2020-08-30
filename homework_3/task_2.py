# 2) Реализовать функцию,принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def quest_func(**kwargs):
    """Сбор данных и вывод их в строку"""
    name = (input('What is your name?')).title()
    surname = (input('What is your surname?')).title()
    born_year = input('What year were you born in?')
    sity = input('What city do you live in?').title()
    email = input('Enter your email: ')
    phone = input('Enter your phone number:')
    print (f'Hello, {name} {surname}! I know that you were born in {born_year}.\n' \
           f'You live in {sity}, right? I`ll write you a letter on {email} \n' \
           f'or call the number {phone}.')


quest_func()
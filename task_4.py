# 4. Пользователь вводит строку из нескольких слов,
# разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если в слово длинное,
# выводить только первые 10 букв в слове.

user_srting = input('Enter a few words through the spacebar: ')

user_srting_list = user_srting.split(' ')

for ind, value in enumerate(user_srting_list, 1):
    print(f'{ind} word - {value[:10]}')


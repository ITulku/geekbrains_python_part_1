# 1. Создать программно файл в текстовом формате,
# записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

f = open('file_for_task_1.txt','x')
f.write('One! \n')
f.write('Two! \n')
f.write('Three! \n')
f.write('Fire!')
f.close()

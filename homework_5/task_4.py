# 4) Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение
# и считывающую построчно данные. При этом английские числительные
# должны заменяться на русские. Новый блок строк должен записываться
# в новый текстовый файл.

def count_prog(file):
    """Замена английских числительныз в файле на русские, с записью в новый файл"""
    rus_num = ['один', 'два', 'три', 'четыре']
    n = 0
    with open(file) as f:
        for i in f:
            line = i.split()
            new_f = open('file_for_task_4_1.txt','a+')
            new_f.write(f'{rus_num[n]} {" ".join(line[1:])} \n')
            n +=1

count_prog('file_for_task_4.txt')
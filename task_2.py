# 2. Создать текстовый файл (не программно),
# сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

def how_many(file):
    """Считает количество строк и слов в каждой строке из файла"""
    f = open(file, 'r')
    lines = 0
    words = 0
    word = 0
    for i in f:
        lines += 1
        for j in i:
            if j == ' ' or j == '\n' :
                words += 1
                word += 1
            if j == '\n':
                print(f'There are {word} words in the {lines} line.')
                word = 0
    print(f'There are {lines} lines in the file.')
    f.close()

how_many('file_for_task_2.txt')

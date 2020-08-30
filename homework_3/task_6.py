# 6) Реализовать функцию ​ int_func()​ , принимающую слово из маленьких
# латинских букв и возвращающую его же, но с прописной первой буквой.
# Например,print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов,
# разделенных пробелом. Каждое слово состоит из латинских букв
# в нижнем регистре. Сделать вывод исходной строки, но каждое слово
# должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию ​ int_func()​ .

def int_func(user_string):
    """Воззвращает строку с первым символов в верхнем регистре"""
    result = user_string.title()
    return result
print(int_func('python'))

def int_func_2(user_string):
    """Возвращает строку из слов с первым символом в верхнем регистре"""
    user_string = user_string.split()
    user_string_list = list(map(int_func, user_string))
    result = ' '.join(user_string_list)
    return result



print(int_func_2('python java javascript ruby go'))
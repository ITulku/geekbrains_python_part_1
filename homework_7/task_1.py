# 1) Реализовать класс ​ Matrix ​ (матрица). Обеспечить перегрузку
# конструктора класса (метод__init__()), который должен принимать данные
# (список списков) для формирования матрицы.
# Подсказка: матрица — ​ система некоторых математических величин,
# расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
# 31 22    3 5 32    3 5 8 3
# 37 43    2 4 6     8 3 7 1
# 51 86   -1 64 -8
# Следующий шаг — реализовать перегрузку метода ​__str__() для вывода матрицы в
# привычном виде.
# Далее реализовать перегрузку метода ​ __add__() для реализации операции
# сложения двух объектов класса ​ Matrix ​ (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно —
# первый элемент первой строки первой матрицы складываем с первым
# элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def printing(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                print(self.matrix[i][j], end='  ')
            print()

    def __str__(self):
        return str(self.printing())

    def __add__(self, other):
        num_str = len(self.matrix)
        num_col = len(other.matrix[0])
        for i in range(num_str):
            for j in range(num_col):
                self.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
            result = self.matrix
        return Matrix(result)





mtx_1 = Matrix([[1, 2], [3, 4], [5, 6], [7, 8]])
mtx_2 = Matrix([[9, 2], [3, 7], [5, 8], [7, 3]])
print(mtx_1)
print(mtx_2)
print(mtx_1 + mtx_2)




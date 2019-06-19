# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

import math


class Triangle:
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C

    def get_lines(self):
        line_1 = math.sqrt(((self.A[0] - self.B[0]) ** 2) + ((self.A[1] - self.B[1]) ** 2))
        line_2 = math.sqrt(((self.A[0] - self.C[0]) ** 2) + ((self.A[1] - self.C[1]) ** 2))
        line_3 = math.sqrt(((self.C[0] - self.B[0]) ** 2) + ((self.C[1] - self.B[1]) ** 2))
        return line_1, line_2, line_3

    def perimeter(self):
        lines = self.get_lines()
        return lines[0] + lines[1] + lines[2]

    def get_square(self):
        pp = self.perimeter()/2
        lines = self.get_lines()
        square = math.sqrt(pp * (pp - lines[0]) * (pp - lines[1]) * (pp - lines[2]))
        return square

    def get_height(self):
        square = self.get_square()
        lines = self.get_lines()
        height = square * 2 / lines[0]

        return height


tr = Triangle([0, 0], [6, 0], [3, 12])
print('периметр  = {}'.format(tr.perimeter()))
print('Площадь = {}'.format(tr.get_square()))
print('высота = {}'.format(tr.get_height()))


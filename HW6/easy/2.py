# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

import math


class Trapeze:
    def __init__(self, A, B, C, D):
        self.A = A
        self.B = B
        self.C = C
        self.D = D

    def get_lines(self):
        line_1 = math.sqrt(((self.A[0] - self.B[0]) ** 2) + ((self.A[1] - self.B[1]) ** 2))
        line_2 = math.sqrt(((self.B[0] - self.C[0]) ** 2) + ((self.B[1] - self.C[1]) ** 2))
        line_3 = math.sqrt(((self.C[0] - self.D[0]) ** 2) + ((self.C[1] - self.D[1]) ** 2))
        line_4 = math.sqrt(((self.D[0] - self.A[0]) ** 2) + ((self.D[1] - self.A[1]) ** 2))
        return line_1, line_2, line_3, line_4

    def get_perimetr(self):
        lines = self.get_lines()
        perimetr = 0
        for line in lines:
            perimetr += line
        return perimetr

    def check(self):
        AB = (self.A[0] - self.B[0]) * (self.A[1] - self.B[1])
        BC = (self.B[0] - self.C[0]) * (self.B[1] - self.C[1])
        DC = (self.D[0] - self.C[0]) * (self.D[1] - self.C[1])
        AD = (self.A[0] - self.D[0]) * (self.A[1] - self.D[1])
        if AB == DC or BC == AD:
            print('Фигура является трапецией')
            if self.get_lines()[0] == self.get_lines()[2] or self.get_lines()[1] == self.get_lines()[3]:
                print('Трапеция равнобедренная')
                # def get_perimetr(self):

    def square(self):
        lines = self.get_lines()
        if lines[0] == lines[2]:
            h = math.sqrt((lines[0] ** 2) - (((abs(lines[1] - lines[3])) / 2) ** 2))
            square = ((lines[1] + lines[3]) / 2) * h
        elif lines[1] == lines[3]:
            h = math.sqrt((lines[1] ** 2) - (((abs(lines[0] - lines[2])) / 2) ** 2))
            square = ((lines[0] + lines[2]) / 2) * h

        return square
Tr = Trapeze([0, 0], [2, 3], [4, 3], [6, 0])

while True:
    print('1 - Проверка фигуры')
    print('2 - Вычисление длин сторон')
    print('3 - Вычисление периметра')
    print('4 - Вычисление площади')
    print('5 - Выход')

    command=input('>>> ')
    if command=='1':
        Tr.check()

    if command=='2':
        print('Длины линий равны соответсвенно: {}'.format(Tr.get_lines()))

    if command=='3':
        print('Периметр={}'.format(Tr.get_perimetr()))

    if command=='4':
        try:
            print('Площадь= {}'.format(Tr.square()))
        except:
            print('Трапеция не равнобедренная')



    if command=='5':
        break



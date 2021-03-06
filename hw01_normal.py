
__author__ = 'Цимборевич Андрей Иванович'

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.


import random

number = int(round(random.random() * 10000, 0))

transform_number = number
print('Заданное число-', number)
find_number=0
count = 0
while count < len(str(number)):
    print_number = transform_number % 10
    if print_number>find_number:
        find_number=print_number
    transform_number = int((transform_number - print_number) / 10)
    count += 1

print(find_number)

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.

a = input('Введите переменную a ')
b = input('Введите переменную b ')
print('Переменная a=', a, ', Переменная b=', b)

print('Трансформирую')

a, b = b, a

print('Переменная a=', a, ', Переменная b=', b)

# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4

import math

a = int(input('Введите коэфициент "a" '))
b = int(input('Введите коэфициент "b" '))
c = int(input('Введите коэфициент "c" '))

discr = b * b - 4 * a * c
if discr < 0:
    print('Уравнение не имеет решения')
else:
    answer1 = (-b + math.sqrt(discr)) / (2 * a)
    answer2 = (-b - math.sqrt(discr)) / (2 * a)
    print('Ответ1= ', answer1, ', ответ2= ', answer2)
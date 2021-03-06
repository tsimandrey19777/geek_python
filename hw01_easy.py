
__author__ = 'Цимборевич Андрей Иванович'

# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.

import random

number = int(round(random.random() * 1000, 0))

transform_number = number
print('Заданное число-', number)

count = 0
while count < len(str(number)):
    print_number = transform_number % 10
    print(print_number)
    transform_number = int((transform_number - print_number) / 10)
    count += 1

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную 
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!


a = input('Введите переменную a ')
b = input('Введите переменную b ')
print('Переменная a=', a, ', Переменная b=', b)


print('Трансформирую')

a, b = b, a

print('Переменная a=', a, ', Переменная b=', b)


# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

age = int(input('Введите Ваш возраст '))

if age < 18:
    print("Извините, пользование данным ресурсом только с 18 лет")
else:
    print("Доступ разрешен")

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

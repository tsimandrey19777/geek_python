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
# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

import random

arr = []
while len(arr) < 10:
    arr.append(int(round(random.random() * 30, 0)))

print(arr)
_index = 0
for number in arr:

    if number % 2 == 0:
        arr[_index] = number / 4
    else:
        arr[_index] = number * 2
    _index += 1
print(arr)

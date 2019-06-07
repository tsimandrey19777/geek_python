# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

import random
import math

arr = []
arr2 = []

while len(arr) < 20:
    arr.append(int(round((random.random() * 150) - 75, 0)))
print(arr)
for number in arr:
    if number < 0:
        continue
    Sqrt = math.sqrt(number)
    if Sqrt // 1 == Sqrt / 1:
        arr2.append(int(Sqrt))

print(arr2)

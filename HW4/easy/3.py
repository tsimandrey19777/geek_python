# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

import random

list_1 = [random.randint(-20, 100) for _ in range(20)]
list_2 = [i for i in list_1 if i % 3 == 0]

list_3 = [i for i in list_1 if i >= 0]
list_4 = [i for i in list_1 if not i % 4 == 0]
print(list_1)
print(list_2)
print(list_3)
print(list_4)


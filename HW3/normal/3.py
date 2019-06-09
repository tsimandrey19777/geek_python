# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


arr = ['a', 'c', '43', 'c', '3', 5, 10, ]
temp = 'c'


def filter_arr(item, temp):
    if item == temp:
        return True
    else:
        return False


arr2 = []
for item in arr:
    if filter_arr(item, temp):
        arr2.append(item)

print(arr2)

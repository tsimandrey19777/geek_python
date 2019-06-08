# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def filter_arr(arr, temp):
    arr2 = []
    for item in arr:
        if item == temp:
            arr2.append(item)
    return arr2

print(filter_arr(['a', 'c', '43', '3', 5, 10], 'c'))


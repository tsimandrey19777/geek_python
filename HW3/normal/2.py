# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

def sort(arr):
    while True:
        count = 0
        for id, item in enumerate(arr):

            if id == 0:
                continue

            if item < arr[id - 1]:
                arr[id], arr[id - 1] = arr[id - 1], arr[id]
                count += 1
        if count == 0:
            break

    return arr


arr = [50, 16, 8, 9, 45]
print(sort(arr))

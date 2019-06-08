# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры1  1

def fibonachi(start, finish):
    row_fibonachi = []
    for position in range(finish):
        if position == 0 or position == 1:
            row_fibonachi.append(1)
        else:
            row_fibonachi.append(row_fibonachi[position - 1] + row_fibonachi[position - 2])
    return row_fibonachi[start - 1:]


start = int(input('Введиту начальную позицию: '))
finish = int(input('Введиту конечную позицию: '))

print(fibonachi(start, finish))


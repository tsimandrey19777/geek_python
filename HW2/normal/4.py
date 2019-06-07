# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут:
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

lst = [1, 2, 3, 4, 51, 2, 3, 4, 5, ]
lst1 = []

lst1.append(lst[0])
for number_lst in lst:
    duble = False
    for number_lst1 in lst1:
        if number_lst == number_lst1:
            duble = True
    if duble:
        continue
    lst1.append(number_lst)
print(lst1)

lst2 = lst

for number in lst:
    count = lst.count(number)

    print(count)
    if count > 1:
        count_temp = 0
        while count_temp < count:
            lst2.remove(number)
            count_temp += 1

print(lst2)

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

a = input('Введите переменную a ')
b = input('Введите переменную b ')
print('Переменная a=', a, ', Переменная b=', b)


print('Трансформирую')

a, b = b, a

print('Переменная a=', a, ', Переменная b=', b)

# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py
import os, shutil
import easy

while True:
    print('1. Перейти в папку')
    print('2. Просмотреть содержимое текущей папки')
    print('3. Удалить папку')
    print('4. Создать папку')
    print('5. Выход')
    command = input('>>> ')
    if command == '5':
        break
    if command == '2':
        print('Текущая папка: ', os.getcwd())
        list = easy.view_dir()
    if command == '1':
        new_dir = input('Введите имя директории: ')
        if new_dir == '/':
            a = os.getcwd().split('\\')[:-1]
            new_dir = '\\'.join(i for i in os.getcwd().split('\\')[:-1])


        try:
            os.chdir(new_dir)
            print('переход осуществлен')
            print('Текущая папка: ', os.getcwd())
        except FileNotFoundError:
            print('переход невозможен - неверный адрес')

    if command == '3':
        name_dir = input('введите название папки: ')
        path = os.path.join(os.getcwd(), name_dir)
        easy.delete_dir(path)
    if command == '4':
        name_dir = input('введите название папки: ')
        path = os.path.join(os.getcwd(), name_dir)
        easy.add_dir(path)

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import mkdir, deletedir
import os, sys

while True:
    print('Для создания директорий введите - "mk"')
    print('Для удаления директорий введите -"rm"')
    print('Для выхода введите - "exit"')
    arg = input('>>> ')
    if arg == 'exit':
        break
    if arg == 'mk':
        name = mkdir.name
        count = mkdir.count
        for i in range(count):
            dir_name=name+'_'+str(i+1)
            path = os.path.join(os.getcwd(), dir_name)
            try:
                os.mkdir(path)
            except FileExistsError:
                print('Директория уже существует')
    if arg == 'rm':
        name = deletedir.name
        count = deletedir.count
        for i in range(count):
            dir_name=name+'_'+str(i+1)
            path = os.path.join(os.getcwd(), dir_name)
            try:
                os.rmdir(path)
            except FileNotFoundError:
                print('Директории уже нет')


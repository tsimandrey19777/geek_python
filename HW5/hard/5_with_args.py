# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3
import os
import sys
import shutil
import glob

print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("cp <filename> - создание копии файла")
    print("rm <filename> -  удаление файла")
    print("cd <full_path or relative_path> -  меняет текущую директорию на указанную")
    print('ls - отображение полного пути текущей директории')

    print("ping - тестовый ключ")


# print("mkdir <dir_name> - создание директории")
def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def ping():
    print("pong")


def copy():
    if not dir_name:
        print('необходимо указать имя файла вторым аргументом')
        return
    dir_path = os.getcwd()
    new_files = 'copy_' + dir_name
    try:
        shutil.copyfile(os.path.join(dir_path, dir_name), os.path.join(dir_path, new_files))
        print('файл {} скопирован'.format(dir_name))
    except FileNotFoundError:
        print('Файл {} не найден'.format(dir_name))


def deletefiles():
    if not dir_name:
        print('Укажите имя файла вторым аргументом')
        return
    dir_path = os.getcwd()
    try:
        confirm = input('Подтвердите удаление файла {}, Y/N'.format(dir_name))
        if confirm == 'Y' or confirm == 'y':
            os.remove(os.path.join(dir_path, dir_name))
    except FileNotFoundError:
        print('Файл не удален, так как отсутвует')


def cd_dir():
    # os.chdir(dir_name)
    if not dir_name:
        print('введите путь во втором аргументе')
        return
    new_dir = dir_name
    if dir_name == '/':
        # a = os.getcwd().split('\\')[:-1]
        new_dir = '\\'.join(i for i in os.getcwd().split('\\')[:-1])

    try:
        print(new_dir)
        os.chdir(new_dir)
        os.walk(new_dir)
        print('переход осуществлен')
        print('Текущая папка: ', os.getcwd())
    except FileNotFoundError:
        print('переход невозможен - неверный адрес')


def ls():
    print(os.getcwd())


do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    'cp': copy,
    'rm': deletefiles,
    'cd': cd_dir,
    'ls': ls
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None

if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")

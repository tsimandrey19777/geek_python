import os, shutil


def view_dir():
    path = os.getcwd()
    list=os.listdir(path)
    return print(list)
def delete_dir(path):
    try:
        shutil.rmtree(path)
        print('Папка с подкаталогами удалена')
    except FileNotFoundError:
        print('Невозможно удалить, папка не существует')
def add_dir(path):
    try:
        os.mkdir(path)
        print('директория создана')
    except FileExistsError:
        print('Невозможно создать- директория уже есть')


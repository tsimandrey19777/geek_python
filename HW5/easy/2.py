# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

import os

dir = os.getcwd()
dirs = os.listdir(dir)
for i in dirs:
    if not os.path.isfile(i):
        print(i)

        
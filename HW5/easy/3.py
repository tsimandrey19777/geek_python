# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import os, sys, shutil

name = sys.argv[0].split('/')
namefiles=name[len(name)-1]
dir =os.getcwd()
newnamefiles='copy_'+namefiles
shutil.copyfile(dir+'/'+namefiles, dir+'/'+newnamefiles)
print(os.listdir(dir))


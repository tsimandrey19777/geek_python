# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.

import os
import random
import re

string = ''
list = [random.randint(0, 9) for _ in range(2500)]
for i in list:
    string = string + str(i)
path = os.path.join('data', 'temp.txt')
with open(path, 'w', encoding='UTF-8') as f:
    f.write(string)
    f.close()

with open(path, 'r', encoding='UTF-8') as f:
    string=f.readline()
    f.close()

temp = []
temp.append(max(re.findall(r'[0]+', string)))
temp.append(max(re.findall(r'[1]+', string)))
temp.append(max(re.findall(r'[2]+', string)))
temp.append(max(re.findall(r'[3]+', string)))
temp.append(max(re.findall(r'[4]+', string)))
temp.append(max(re.findall(r'[5]+', string)))
temp.append(max(re.findall(r'[6]+', string)))
temp.append(max(re.findall(r'[7]+', string)))
temp.append(max(re.findall(r'[8]+', string)))
temp.append(max(re.findall(r'[9]+', string)))
len_str = 0
a=''
for i in temp:
    if len(i)>len_str:
        len_str=len(i)
        a=i
print(a)


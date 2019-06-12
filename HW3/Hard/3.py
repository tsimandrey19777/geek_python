# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))
import os


def get_fruits_in_files():
    path = os.path.join('data', 'fruits.txt')
    f = open(path, 'r', encoding='UTF-8')
    for fruits in f.readlines():
        if fruits[0].isalpha():
            path_fruit = os.path.join('data/fruits', 'fruits_{}'.format(fruits[0].capitalize()))

            file = open(path_fruit, 'a', encoding='UTF-8')
            file.write(fruits)
            file.close()

get_fruits_in_files()
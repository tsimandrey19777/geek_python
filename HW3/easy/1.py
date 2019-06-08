# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def round_num (number, decimal_places):
    position = str(number).index('.')
    round_number = float(number[:position + decimal_places + 1])
    if int(number[position + decimal_places + 1]) >= 5:
        round_number = round_number + (1 / (10 ** decimal_places))

    return round_number


number = input('Введите число: ')
decimal_places = int(input('Введите количество знаков после запятой: '))

print(round_num(number, decimal_places))




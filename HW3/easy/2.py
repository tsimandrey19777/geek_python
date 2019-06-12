# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def luck_number(number):
    num = []
    if len(number) != 6 or not number.isdigit():
        return 'uncorrect'
    for n in number:
        num.append(int(n))
    if sum(num[:3]) == sum(num[3:]):
        return 'luck'

    else:
        return 'not luck'

number = input('Введите шестизначный номер билета: ')
print(luck_number(number))

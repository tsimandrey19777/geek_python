# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3
import math

exp = '-3 2/3 - -2 1/2'


def get_list_exp(string):
    ''' возвращает строку в виде списка'''
    return string.split(' ')


def get_sign():
    '''Возвращает позицию знака и знак'''
    list = get_list_exp(exp)
    for id, item in enumerate(list):
        if item == '+' or item == '-' or item == '*' or item == '/':
            return id, item


def get_variables():
    list = get_list_exp(exp)
    id = get_sign()[0]
    variables_1 = []
    variables_2 = []

    if id == 2:
        var_1 = list[1].split('/')
        variables_1.append(int(list[0]))
    elif id == 1:
        var_1 = list[0].split('/')
    variables_1.append(int(var_1[0]))
    variables_1.append(int(var_1[1]))

    if len(list) - id == 3:
        var_2 = list[id + 2].split('/')
        variables_2.append(int(list[id + 1]))
    elif len(list) - id == 2:
        var_2 = list[id + 1].split('/')
    variables_2.append(int(var_2[0]))
    variables_2.append(int(var_2[1]))

    return variables_1, variables_2


def get_fraction(variable):
    if len(variable) == 2:
        return [variable[0], variable[1]]
    elif len(variable) == 3:
        if variable[0] < 0:
            return [((abs(variable[0]) * variable[2]) + variable[1]) * -1, variable[2]]
        else:
            return [(variable[0] * variable[2]) + variable[1], variable[2]]


def get_variables_for_nok():
    var1 = get_fraction(get_variables()[0])
    var2 = get_fraction(get_variables()[1])
    nok = var1[1] * var2[1] // math.gcd(var1[1], var2[1])
    n_1 = nok / var1[1]
    n_2 = nok / var2[1]
    var1[0] = int(var1[0] * n_1)
    var1[1] = nok
    var2[0] = int(var2[0] * n_2)
    var2[1] = nok
    return var1, var2

    # def fraction(list, id):


#     if id == 1:
#         numerator = int(list.split('/')[0])
#         denominator=int(list.split('/')[1])
#         integer=int

# exp2 = get_list_exp(exp)
# print(exp2)
# sign = get_sign(exp2)
# print(get_sign(exp2)[0])
# var = get_variables()
# print(var[0])
# print(var[1])
# a=get_fraction(var[0])
# b=get_fraction(var[1])
# print(get_variables_for_nok())

sign = get_sign()[1]
answer = []
if sign == '+' or sign == '-':
    var1 = get_variables_for_nok()[0]
    var2 = get_variables_for_nok()[1]
    if sign == '+':
        answer.append(var1[0] + var2[0])
        answer.append(var1[1])
    else:
        answer.append(var1[0] - var2[0])
        answer.append(var1[1])
elif sign == '*' or sign == '/':
    var1 = get_variables()[0]
    var2 = get_variables()[1]
    if sign == '*':
        answer.append(var1[0] * var2[0])
        answer.append(var1[1] * var2[1])
    else:
        answer.append(var1[0] * var2[1])
        answer.append(var1[1] * var2[0])


def get_optimal_answer(answer):
    if abs(answer[0]) > answer[1]:
        if answer[0] < 0:
            return '-{} {}/{}'.format(abs(answer[0]) // answer[1], abs(answer[0]) % answer[1], answer[1])
        else:
            return '{} {}/{}'.format(answer[0] // answer[1], answer[0] % answer[1], answer[1])
    else:
        return '{}/{}'.format(answer[0], answer[1])


print(get_optimal_answer(answer))

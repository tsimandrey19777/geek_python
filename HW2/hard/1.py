# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.

equation = 'y = -12x + 11111140.2121'
x = 2.5
# вычислите и выведите y
x_index = equation.find('x')
r = equation.find('=')

K = float(equation[equation.find('=') + 1:equation.find('x')])
B_temp = equation[equation.find('x') + 1:]
sign = B_temp[:2]

if sign == ' +' or sign == '+ ':
    sig = 1
if sign == ' -' or sign == '- ':
    sig = -1
B = (float(B_temp[2:]))
y = K * x + B * sig

print(y)

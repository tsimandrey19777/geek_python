# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

def delta(A, B):
    delta_x = A[0] - B[0]
    delta_y = A[1] - B[1]

    return delta_y, delta_y


def parallel_check(A1, A2, A3, A4):
    if delta(A1, A2) == delta(A4, A3) and delta(A1, A4) == delta(A2, A3):
        return True
    else:
        return False


A1 = (4, -3)
A2 = (8, -7)
A3 = (7, -10)
A4 = (3, -6)

print(parallel_check(A1, A2, A3, A4))

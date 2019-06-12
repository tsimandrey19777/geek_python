# Задание-3 (Ферзи):
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били
# друг друга. Вам дана расстановка 8 ферзей на доске.
# Определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел,
# каждое число от 1 до 8 — координаты 8 ферзей.
# Если ферзи не бьют друг друга, выведите слово NO, иначе выведите YES.


x = [[5, 1], [7, 2], [2, 3], [6, 4], [3, 5], [1, 6], [4, 7], [8, 8]]


def render():
    board = []
    for i in range(8):
        board.append([])
        for j in range(8):
            board[i].append(0)
    return board


def arrangement(figures):
    board = render()
    for i in figures:
        # print(i)
        board[i[0] - 1][i[1] - 1] = 1
    return board


def get_diagonal(board):
    diagonal = []
    for i in range(0, 7):
        diagonal.append([])
        for j in range(8 - i):
            diagonal[i].append(board[i + j][j])
    for j in range(1, 7):
        diagonal.append([board[i][j + i] for i in range(8 - j)])
        # for i in range(8 - j):
        #     diagonal[].append(board[i][j+i])

    return diagonal


def get_board_reverse(board):
    return list(map(list, zip(*board)))


def get_board_mirror(board):
    board_mirror = []
    for i in range(8):
        board_mirror.append([])
        for j in range(8):
            board_mirror[i].append(board[i][7-j])

    return board_mirror


def check(board):
    board_reverse = get_board_reverse(board)
    for i in board:
        if sum(i) > 1:
            return print('No')
    for j in board_reverse:
        if sum(j) > 1:
            return print('No')

    for i in get_diagonal(board):
        if sum(i) > 1:
            return print('No')
    for i in get_diagonal(get_board_mirror(board)):
        if sum(i) > 1:
            return print('No')

    return print('Yes')


check(arrangement(x))

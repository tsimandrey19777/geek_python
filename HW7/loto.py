"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87
      16 49    55 77    88
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html

"""
import random


class card:
    def __init__(self, string_1, string_2, string_3):
        self.string_1 = string_1
        self.string_2 = string_2
        self.string_3 = string_3

    def CreateCard(self):
        self.string_1 = [' ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ']
        self.string_2 = [' ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ']
        self.string_3 = [' ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ']
        count = 0
        while True:

            if count == 15:
                break
            number = random.randint(1, 90)
            if number in self.string_1 or number in self.string_2 or number in self.string_3:
                continue
            if number // 10 == 9:
                index = 8
            else:
                index = number // 10
            if not type(self.string_1[index]) == int:
                self.string_1[index] = number
                count += 1
            elif not type(self.string_2[index]) == int:
                self.string_2[index] = number
                count += 1
            elif not type(self.string_3[index]) == int:
                self.string_3[index] = number
                count += 1
            else:
                continue
        # print(self.string_1)
        # print(self.string_2)
        # print(self.string_3)

        # return self.string_1, self.string_2, self.string_3

    def __str__(self):
        str_1 = ''
        str_2 = ''
        str_3 = ''
        for i in range(9):
            str_1 = str_1 + ' ' + str(self.string_1[i])
            str_2 = str_2 + ' ' + str(self.string_2[i])
            str_3 = str_3 + ' ' + str(self.string_3[i])

        return '{}\n{}\n{}\n{}'.format(str_1, str_2, str_3, '-' * 35)

    def CheckAvailability(self, number):
        if number in self.string_1 or number in self.string_2 or number in self.string_3:
            # print('Есть')
            if number in self.string_1:
                self.string_1[self.string_1.index(number)] = '-' * len(str(number))
            elif number in self.string_2:
                self.string_2[self.string_2.index(number)] = '-' * len(str(number))
            elif number in self.string_3:
                self.string_3[self.string_3.index(number)] = '-' * len(str(number))
            return True
        else:
            return False

    def CheckAllAvailable(self):
        flag = 0
        for i in range(9):
            if type(self.string_1[i]) == int or type(self.string_2[i]) == int or type(self.string_3[i]) == int:
                flag = 1
        if flag == 1:
            return True
        else:
            return False


player = card('', '', '')
player.CreateCard()
com_player = card('', '', '')
com_player.CreateCard()


def print_card():
    print('{}Ваша карточка{}'.format('-' * 11, '-' * 11))
    print(player)
    print('{}Карточка компьютера{}'.format('-' * 8, '-' * 8))
    print(com_player)


def GenerateNumberFishri(list_fishki):
    while True:
        number = random.randint(1, 90)
        if number in list_fishki:
            continue
        list_fishki.append(number)
        return number


def startGame():
    list_fishki = []
    # print_card()
    # if input('Поехали! Y/N') != 'Y':
    #     return
    while True:
        print_card()

        number = GenerateNumberFishri(list_fishki)
        print(list_fishki)
        print(list_fishki[-1])

        answer = input('Бочонок №{}. Подтверждаете: Y/N '.format(number))

        com_player.CheckAvailability(number)
        if answer == 'Y' or answer == 'y':
            if player.CheckAvailability(number):
                if player.CheckAllAvailable():
                    if com_player.CheckAllAvailable():
                        continue
                    else:
                        print('Вы проиграли, так как компьютер выйграл')
                        return
                else:
                    print('Вы выйграли!!!')
                    return
            else:
                print('Вы проиграли, так как подтвержденного Вами числа не найдено в Вашей карточке')
                return
        else:
            if not player.CheckAvailability(number):
                if com_player.CheckAllAvailable():
                    continue
                else:
                    print('Вы проиграли, так как компьютер вйграл!!!')
                    return
            else:
                print('Вы проиграли, так как число, которое вы не подтвердили присутсвует в Вашей карточке')
                return


startGame()

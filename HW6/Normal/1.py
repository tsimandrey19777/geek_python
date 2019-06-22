# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе


class Person():
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name

    def get_full_name(self):
        return self.name + ' ' + self.last_name


class Disciple(Person):
    def __init__(self, name, last_name, class_room, number_for_disciple):
        super().__init__(name, last_name)
        self.class_room = {'class_num': int(class_room[0:-1]), 'class_char': class_room[-1]}
        self.number_for_disciple = number_for_disciple

    def get_class_room(self):
        return str(self.class_room['class_num']) + self.class_room['class_char']




class Teacher(Person):
    def __init__(self, name, last_name, lesson_name, class_row):
        super().__init__(name, last_name)
        self.lesson_name = lesson_name
        self.class_row = list(map(self.convert_class, class_row))

    def convert_class(self, class_room):
        return {'class_num': int(class_room[0:-1]), 'class_char': class_room[-1]}

    def get_class_row(self):
        classes = []
        for i in self.class_row:
            # print('{}{}'.format(i['class_num'], i['class_char']))
            classes.append(str(i['class_num']) + i['class_char'])
        return classes




class Parent_mather(Person):
    def __init__(self, name, last_name, number_for_disciple):
        super().__init__(name, last_name)
        self.number_for_disciple = number_for_disciple




class Parent_father(Person):
    def __init__(self, name, last_name, number_for_disciple):
        super().__init__(name, last_name)
        self.number_for_disciple = number_for_disciple




disciples = [Disciple('Иван', 'Иванов', '5A', 1),
             Disciple('сергей', 'сергеев', '6A', 2)]
teachers = [Teacher('Ольга', 'Ивановна', 'математика', ('5A', '6A')),
            Teacher('Яна', 'Игорьевна', 'литература', ('5A', '6A'))]

mathers = [Parent_mather(name='Ольга', last_name='Иванова', number_for_disciple=1),
           Parent_mather(name='Ирина', last_name='Сергеева', number_for_disciple=2),
           ]

fathers = [Parent_father(name='Илья', last_name='Иванов', number_for_disciple=1),
           Parent_father(name='Игнат', last_name='Сергеев', number_for_disciple=2), ]


def get_all_clases():
    classes = []
    for discipl in disciples:
        if not discipl.get_class_room() in classes:
            classes.append(discipl.get_class_room())
    return classes


def get_all_disciples():
    all_disciples = []
    for i in disciples:
        all_disciples.append(i.get_full_name())
    return all_disciples


def get_class(full_name):
    for i in disciples:
        if full_name.split()[0] == i.name and full_name.split()[1] == i.last_name:
            return str(i.get_class_room())


def get_numer(full_name):
    for i in disciples:
        if full_name.split()[0] == i.name and full_name.split()[1] == i.last_name:
            return i.number_for_disciple


while True:
    print('1. Получить полный список всех классов школы')
    print('2. Получить список всех учеников в указанном классе')
    print('3. Получить список всех предметов указанного ученика')
    print('4. Узнать ФИО родителей указанного ученика')
    print('5. Получить список всех Учителей, преподающих в указанном классе')
    print('6. Выход')
    command = input('>>> ')

    if command == '1':
        print(get_all_clases())
    if command == '2':
        find_class = input('Введите класс, например 5А: ')
        if find_class in get_all_clases():
            for discipl in disciples:
                if discipl.get_class_room() == find_class:
                    print(discipl.get_full_name())

        else:
            print('Введеного класса нет в школе')
    if command == '3':
        name_discipl = input('Введите имя и фамилию ученика: ')
        if name_discipl in get_all_disciples():
            for teacher in teachers:
                # print(get_class(name_discipl))
                # print(teacher.get_class_row())

                if get_class(name_discipl) in teacher.get_class_row():
                    print(teacher.lesson_name)
        else:
            print('Ученик не найден')

    if command == '4':
        name_discipl = input('Введите имя и фамилию ученика: ')
        if name_discipl in get_all_disciples():
            for i in mathers:
                if i.number_for_disciple == get_numer(name_discipl):
                    print(i.get_full_name())
            for i in fathers:
                if i.number_for_disciple == get_numer(name_discipl):
                    print(i.get_full_name())
        else:
            print('Ученик не найден')

    if command=='5':
        find_class = input('Введите класс, например 5А: ')
        if find_class in get_all_clases():
            for teacher in teachers:
                if find_class in teacher.get_class_row():
                    print(teacher.get_full_name())

        else:
            print('Введеного класса нет в школе')
    if command == '6':
        break

# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла
import os


class worker():
    def __init__(self, name, last_name, salary, staff, norm, hours, fact_salary):
        self.name = name
        self.last_name = last_name
        self.salary = salary
        self.staff = staff
        self.norm = norm
        self.hours = hours
        self.fact_salary = fact_salary

    def get_full_name(self):
        return self.name + ' ' + self.last_name

    def set_fact_salary(self):
        if self.hours < self.norm:
            self.fact_salary = round((self.salary / self.norm) * self.hours, 0)
        elif self.hours == self.norm:
            self.fact_salary = self.salary
        elif self.hours > self.norm:
            self.fact_salary = round(self.salary + ((self.salary / self.norm) * (self.hours - self.norm)) * 2, 0)




    def print_salary(self, n):
        print(self.get_full_name() + ' ' * (n - len(self.get_full_name())) + self.fact_salary)


def get_Workers():
    path = os.path.join('data', 'workers')
    with open(path, 'r', encoding='UTF-8') as f:
        workers = f.readlines()
        f.close()

    Workers = []

    for id, work in enumerate(workers):
        if id == 0:
            continue
        if work[:-2] == '\\n':
            work = work[:-2].split()
        else:
            work = work.split()

        Workers.append(worker(work[0], work[1], int(work[2]), work[3], int(work[4]), 0, 0))

    get_hours(Workers)
    return Workers


def get_hours(Workers):
    path = os.path.join('data', 'hours_of')
    with open(path, 'r', encoding='UTF-8') as f:
        hours = f.readlines()
        f.close()
    for id, item in enumerate(hours):
        if id == 0:
            continue
        if item[:-2] == '\\n':
            item = item[:-2].split()
        else:
            item = item.split()
        for worker in Workers:
            if item[0] + ' ' + item[1] == worker.get_full_name():
                worker.hours = int(item[2])
                worker.set_fact_salary()


def get_n():
    n = 0
    for work in get_Workers():
        if len(work.get_full_name()) > n:
            n = len(work.get_full_name())
    return n


def print_salary():
    print('Работник'+' '*(get_n()-7)+'Зарплата')
    for i in get_Workers():
        print(i.get_full_name() + ' ' * (get_n() - len(i.get_full_name()) + 1) + str(i.fact_salary))


print_salary()

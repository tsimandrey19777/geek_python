# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"
import os


def get_workers():
    path = os.path.join('data', 'workers')
    f = open(path, 'r', encoding='UTF-8')
    workers = []
    for id, line in enumerate(f.readlines()):
        if id == 0:
            continue
        temp = line.split(' ')
        temp = list(filter(lambda x: x != '', temp))
        # print(temp)
        workers.append({})
        workers[id - 1]['name'] = temp[0] + ' ' + temp[1]
        # workers[id - 1]['last_name'] = temp[1]
        workers[id - 1]['salary'] = int(temp[2])
        workers[id - 1]['position'] = temp[3]
        workers[id - 1]['norma'] = int(temp[4].replace('\n', ''))
    f.close()
    return workers


def get_hours():
    path = os.path.join('data', 'hours_of')
    f = open(path, 'r', encoding='UTF-8')
    hours = []

    for id, line in enumerate(f.readlines()):
        if id == 0:
            continue
        hours.append({})
        temp = line.split(' ')
        temp = list(filter(lambda x: x != '', temp))
        hours[id - 1]['name'] = temp[0] + ' ' + temp[1]
        # hours[id - 1]['last_name'] = temp[1]
        hours[id - 1]['hours'] = int(temp[2].replace('\n', ''))
    f.close()
    return hours


def get_fact_salary():
    fact_salary = []

    for id, hours in enumerate(get_hours()):
        for worker in get_workers():
            if hours['name'] == '':
                break
            if hours['name'] == worker['name']:
                fact_salary.append({})
                salary = worker['salary']
                norma = worker['norma']
                hour = hours['hours']
                if norma >= hour:
                    f_salary = (salary / norma) * hour
                else:
                    f_salary = salary + (hour - norma) * (salary / norma) * 2
                fact_salary[id]['name'] = hours['name']
                fact_salary[id]['salary'] = int(round(f_salary, 0))
                break
    # print(get_hours()[len(get_hours()) - 1])
    return fact_salary


def print_salary():
    print('{:<20} {}'.format('Имя', 'Зарплата'))
    long = 20
    for item in get_fact_salary():
        if len(item['name']) > long:
            long = len(item['name'])
    for item in get_fact_salary():
        print('{:<20} {}'.format(item['name'], item['salary']))


print(print_salary())

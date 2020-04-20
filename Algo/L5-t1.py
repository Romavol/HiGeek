'''
Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого
 предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования
  предприятий, чья прибыль выше среднего и ниже среднего.
'''

from collections import namedtuple

Nna = 'ff'
Npp = 0
comp = namedtuple('comp1', 'name, Q1, Q2, Q3, Q4, IY')
tlist = []
while Nna != '0':
    Nna = input('Введите имя Фирмы, для выхода - 0 :')
    if Nna != '0':
        spam = input('Доход по кварталам через пробел: Q1 Q2 Q3 Q4 :').split()
        if len(spam) == 4:
            iy = float(spam[0]) + float(spam[1]) + float(spam[2]) + float(spam[3])
            tlist.append(comp(Nna, float(spam[0]), float(spam[1]), float(spam[2]), float(spam[3]), iy))
            Npp += iy
        else:
            print('Доходы не распознаны. Введите заново. ')

Npp = Npp / len(tlist)
print(f'Средний доход {len(tlist)} фирм = {Npp}')

for i in tlist:
    if i.IY < Npp:
        print(f'Доход " {i.name} " меньше среднего, = {i.IY}')
    elif i.IY > Npp:
        print(f'Доход " {i.name} " БОЛЬШЕ среднего, = {i.IY}')

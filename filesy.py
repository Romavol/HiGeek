# --------- 1 ------------------------------------------------------------

with open('test1.txt', 'w') as fi:
    while True:
        sss = input('Введите слова для файла. Пробел - выход :')
        if sss == ' ':
            break
        else:
            fi.write(sss + '\n')

# ---------- 2 --------

import json

# Заодно поработаем с жсоном

with open('test1.txt') as fi:
    alll = fi.readlines()
    print(' Кол-во строк в файле = ', len(alll))
    datj = dict()
    lcount = 0
    for i in alll:
        stro = i.split()
        lcount += 1
        print(f' В строке {lcount} слов = {len(stro):.0f}  , это ', stro)
        datj.update({'line' + str(lcount): stro})

fj = open('fiji.json', 'w')
json.dump(datj, fj)
fj.close()

# ------- 3 ----------------------------------

# Файл для анализа :
# Иванов 13
# петров 14
# сидовов 20
# Епп 25


with open('sala.txt', encoding='utf-8', newline='') as fi:
    alll = fi.readlines()

asum = 0
for (nn, i) in enumerate(alll):
    stro = i.split()
    asum += int(stro[1])
    if int(stro[1]) < 15:
        print(f' Менее 15 зп : {stro[0]} , ', stro[1])

print(f' -- Итого средняя ЗП по {nn + 1} сотрудникам составляет {asum / (nn + 1):.2f}')
##     nums = map(int, nums.split())  # without list
#     sum_nums = sum(nums)

# ----------- 4 -------------

m_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

f1 = open('one.txt', 'r', encoding='utf-8')
with open('one2.txt', 'w', encoding='utf-8') as fi:
    for line in f1:
        lis = line.split()
        # fi.write()
        print(m_dict.get(lis[0]), lis[1], lis[2], file=fi)

f1.close()

# ------- 5 --------------------------------------------

asum = 0
with open('test1.txt', 'w') as fi:
    for i in range(1, 10, 2):
        fi.write(str(i) + '  ')
        asum += i

print('Вся сумма = ', asum)

# ---------- 6 ---------------------------------------------
'''
# Информатика:   100(л)   50(пр)   20(лаб).
# Физика:   30(л)   —   10(лаб)
# Физкультура:   —   30(пр)
'''

with open('test1.txt', encoding='utf-8') as fi:
    alll = fi.readlines()

my_dict = dict({})
for i in alll:  # по строкам
    ss1 = i.split()
    asum = 0
    for ss in ss1:  # по словам строки
        xx = 0
        s_digi = '0'
        for bb in ss:
            s_digi = s_digi + bb if bb.isdigit() else s_digi
        asum += int(s_digi)
    my_dict.update({(ss1[0])[:-1]: asum})

print(my_dict)
# re.findall('\d{1,}', you_str)  /d+
##         sum_lessons = sum([int(x[:x.find('(')]) for x in splitted_line[1:] if '(' in x])

# ---------- 7 -----------------
# firm_1   ООО   10000   5000
# firm_2   IP    11000   6500
# firm_3   OOO   80000  82000
# firm_4   IP    20000  15000

import json

with open('test1.txt', encoding='utf-8') as fi:
    alll = fi.readlines()

my_dict = dict({})
asum = 0
for (nn, i) in enumerate(alll):  # по строкам
    ss1 = i.split()
    profit = float(ss1[2]) - float(ss1[3])
    asum += profit
    if profit > 0:
        my_dict.update({ss1[0]: profit})

my_list = [my_dict, dict({'average_profit': asum / (nn + 1)})]

with open('fiji.json', 'w') as fj:
    json.dump(my_list, fj)

##         name, form, revenue, costs = line.split()

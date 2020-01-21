

# --------- 1 ------------------------------------------------------------

with open('test1.txt', 'w') as fi:
    while True:
        sss = input('Введите слова для файла. Пробел - выход :')
        if sss == ' ':
            break
        else:
            fi.write(sss+'\n')

# ---------- 2 --------

import json
# Заодно поработаем с жсоном

with open('test1.txt') as fi:
    alll = fi.readlines()
    print(' Кол-во строк в файле = ', len(alll))
    datj = dict()
    lcount=0
    for i in alll:
        stro = i.split()
        lcount+=1
        print(f' В строке {lcount} слов = {len(stro):.0f}  , это ', stro)
        datj.update({'line'+str(lcount): stro})

fj = open('fiji.json', 'w')
json.dump(datj, fj)
fj.close()



# ------- 3 ----------------------------------
'''
Файл для анализа :
Иванов 13
петров 14
сидовов 20
Епп 25
'''

with open('sala.txt', encoding='utf-8', newline='') as fi:
    alll = fi.readlines()

asum = 0
for (nn, i) in enumerate(alll):
    stro = i.split()
    asum += int(stro[1])
    if int(stro[1]) < 15:
        print(f' Менее 15 зп : {stro[0]} , ', stro[1])

print(f' -- Итого средняя ЗП по {nn+1} сотрудникам составляет {asum/(nn+1):.2f}')



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

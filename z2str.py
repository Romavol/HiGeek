# Решение по уроку 2
#
'
# Задание 1
spis=[12, 12.45, 'Noone', 3>2, (12,123,34)]
for i in spis:
    print(i,"  ",type(i))

# ----2-----


list2 = []
len_list = int(input('Сколько будет переменных ?'))
while len(list2) < len_list:
    list2.append(input(' Введите значение для обмена :'))

len_list = len_list-1 if len_list%2 else len_list # Проверка на нечентый список

i=0
while i < len_list:
    temp_l=list2[i]
    list2[i] = list2[i+1]
    list2[i+1]=temp_l
    i+=2
    # чудоконструкцию xx,yy=11,22 я еще не выучил. поэтому тупой обход. Ну и без range пробовал.
print('Получилось : ',list2)

#------- 3 ---------------

while True:
    mons = int(input(' Введи месяц : '))
    if mons > 0 and mons < 12 :
        break
    else: print('Неподходящее число. Повторим.')

m_list = ['', 'зима', 'зима', 'весна', 'весна', 'весна', 'лето', 'лето', 'лето', 'осень', 'осень', 'осень', 'зима']
m_dict = {1: 'зима', 2: 'зима', 3: 'весна', 4: 'весна', 5: 'весна', 6: 'лето', 7: 'лето', 8: 'лето', 9: 'осень',
          10: 'осень', 11: 'осень', 12: 'зима'}
print(' Месяц list ', mons, ' = ', m_list[mons])
print(' Месяц dict ', mons, ' = ', m_dict.get(mons))


# ------- 4 --------------------

text = input('Введите многословное предложение : ')
list_txt = text.split()
for i, stro in enumerate(list_txt, start=1):
    print(i, stro[:10])


# ---- 5 ------------------


stru = [7, 6, 4, 3, 1]
while True:
    vvo = int(input(' Введите число до 10. 0 = Завершить : '))

    if vvo == 0: break
    max_d = 0
    for i in range(len(stru)):
        if vvo >= stru[i]:
            stru.insert(i, vvo)
            break

print(stru)

# ---- 6 ------------------


list = []
diss = {'название', 'цена', 'количество'}
i = 1
dic_tmp = dict(цена='1')

while i < 3:
    for name in diss:
        tex_inp = 'Введите ' + str(i) + ' - ' + name + ' : '
        dic_tmp[name] = input(tex_inp)

    list.append((i, dic_tmp.copy())) # без копии неверно работало...
    i += 1

for i in list:
    print(i)

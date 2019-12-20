# ###
#
#
# #
#
#
# var_num = 12 + 4
# var_str = "Some string ."
#
# print("1. var num = " , str(var_num), ' and summ 220 + 45 is ' , 220+45)
# print("1. " + var_str)
#
#
# user = input(" Введи свой никНейм : ")
# week = int(input(" Введи сегодняшний день  недели числом : "))
#
# if week < 0:
#    print(" Чтото пошло не так с числом...")
# elif week == 1: print(user,", сегодня Пнд.")
# elif week == 2: print(user, " , сегодня Втр.")
# elif week == 3: print(user, " , сегодня Срд.")
# elif week == 4: print(user, " , сегодня Четв.")
# elif week == 5: print(user, " , сегодня Пятн.")
# else: print(user, " , вот и Выходной.")
#
# # часть 2
#
# secu = int(input(" 2. Введи мноого секунд. Например с утра : "))
# hours = secu//3600
#
# minutes = (secu - (3600 * hours))//60
# secunds = (secu - (3600 * hours + minutes * 60))
#
# print( hours, minutes, secunds, sep=':')
#
#
# # Часть 3
#
# snum1 = input("3. Введи число n до 10 :")
# snum2 = snum1+snum1
# snum3 = snum2+snum1
#
#
#
# print("3. Сумма 3х Чисел ( n + nn + nnn ) равна = ", int(snum1)+int(snum2)+int(snum3))
#
#
# num = input("4. Введи целое положительное многозначное число  :")
# maxn=0
# a=0
# lenstr=len(num)
#
# while a < lenstr :
#  #   print(num[a])
#     if maxn<int(num[a]) : maxn=int(num[a])
#     a += 1
#
# print('4. Cамая большая цифра в числе : ', maxn)
#
#
#
# income = int(input("5 . Введите сумму выручки фирмы : "))
# expenses = int(input("5 . Введите сумму издержек фирмы : "))
# pri = income - expenses
#
# if income < expenses:
#     print("   Фирма показывает убыток. Рассчитывать нечего...")
# else:
#     print("  Фирма показывает прибыль. ")
#     print("  Рентабельность составляет ", str(100*pri/income), "%")
#     empl=int(input("  Введите численность работников : "))
#     print("  Прибыль на одного работника  ", "{:.2f}".format(pri / empl,2))
#
#
#
#
#
# rez_a = int(input("6 . Введите 1й начальный результат в км : "))
# rez_b = int(input("6 . Введите 2й целевой результат в км : "))
# a = 1
# while rez_a < rez_b:
#     rez_a *= 1.1
#     a += 1
#
#
# print('6 . целевой результат достигнут на ', a, ' день')
#
#
#
#

'''
Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как коллекция,
 элементы которой — цифры числа
'''

from collections import namedtuple

n1c = []
n2c = []
Heh = namedtuple('Heh', ['A', 'B', 'C', 'D', 'E', 'F'])
hes = Heh(10, 11, 12, 13, 14, 15)
n1 = input('Введите 1е шеснадцатиричное слагаемое : ')
n2 = input('Введите 2е шеснадцатиричное слагаемое : ')
for i in n1:
    if i in '0123456789':
        n1c.append(int(i))
    elif i.upper() == 'A':  # Не нашел как сделать красивее.
        n1c.append(hes.A)
    elif i.upper() == 'B':
        n1c.append(hes.B)
    elif i.upper() == 'C':
        n1c.append(hes.C)
    elif i.upper() == 'D':
        n1c.append(hes.D)
    elif i.upper() == 'E':
        n1c.append(hes.E)
    elif i.upper() == 'F':
        n1c.append(hes.F)
    else:
        n1c.append(0)  # заглушка .

for i in n2:
    if i in '0123456789':
        n2c.append(int(i))
    elif i.upper() == 'A':  # Не нашел как сделать красивее.
        n2c.append(hes.A)
    elif i.upper() == 'B':
        n2c.append(hes.B)
    elif i.upper() == 'C':
        n2c.append(hes.C)
    elif i.upper() == 'D':
        n2c.append(hes.D)
    elif i.upper() == 'E':
        n2c.append(hes.E)
    elif i.upper() == 'F':
        n2c.append(hes.F)
    else:
        n2c.append(0)  # заглушка .

print(n1c)
print(n2c)

 if len(n2c) > len(n1c):
     n1c, n2c = n2c, n1c

rez = []
n1c = n1c[::-1]
n2c = n2c[::-1]
for i in n1c:



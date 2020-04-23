'''
Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как коллекция,
 элементы которой — цифры числа
'''

from collections import defaultdict

n1c = []
n2c = []
obr = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
list_of_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

n1 = input('Введите 1е шеснадцатиричное слагаемое : ')
n2 = input('Введите 2е шеснадцатиричное слагаемое : ')
for i in n1:
    if i in '0123456789':
        n1c.append(int(i))
    elif i.upper() in 'ABCDEF':
        n1c.append(obr[i.upper()])
    else:
        n1c.append(0)  # заглушка .

for i in n2:
    if i in '0123456789':
        n2c.append(int(i))
    elif i.upper() in 'ABCDEF':
        n2c.append(obr[i.upper()])
    else:
        n2c.append(0)  # заглушка .

# print(n1c)
# print(n2c)

if len(n2c) > len(n1c):
    n1c, n2c = n2c, n1c

rez = []
n1c = n1c[::-1]
n2c = n2c[::-1]
k = 0
addr = 0
for i in n1c:
    if len(n2c) < (k + 1):
        spam = i + addr
    else:
        spam = i + n2c[k] + addr
    rez.append(list_of_numbers[spam % 16])
    if spam > 15:
        addr = 1
    else:
        addr = 0
    k += 1
if addr == 1:
    rez.append('1')

n1 = ''
print('- - - - - - - ')

print('Итого : ',''.join(rez[::-1]))

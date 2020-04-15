'''
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
'''

rez = [0 for _ in range(0, 10)]

for i in range(2, 99 + 1):

    for n in range(2, 10):
        if not i % n:
            rez[n] += 1
rez.pop(0)
rez.pop(0)
print(*rez, sep=' -- ')

'''

Нахождение простых чисел
ЗААТУПИЛ ! ЭТО ПРОСТО НАХОЖДЕНИЕ Сейчас переделаю на функции...
нахождения i-го по счёту простого числа.
'''

import timeit
import cProfile
import math

NN = 2000000


# Алгоритм - тупарь. Пройдемся, просеим. Без затей.
def primes(ns):
    n = int(ns)
    a = [0] + list(range(1, NN))
    a[1] = 0
    rezfind = 1
    m = 1
    while m < NN:  # перебор всех элементов до заданного числа
        spam = a[m]
        if a[m] != 0:  # если он не равен нулю, то
            if rezfind == n:
                return a[m]
            else:
                rezfind += 1

            j = m * 2  # увеличить в два раза (текущий элемент простое число)
            while j < NN:
                a[j] = 0  # заменить на 0
                j = j + m  # перейти в позицию на m больше
        m += 1

    b = []
    for i in a:
        if a[i] != 0:
            b.append(a[i])

    return 0


# идея в вычитании множеств - 2ек умнорженных и т.д..
def primes2(NS):
    N = int(NS)
    """Возвращает все простые от 2 до N"""
    sieve = set(range(2, NN))
    for i in range(2, int(math.sqrt(NN))):
        if i in sieve:
            sieve -= set(range(2 * i, NN, i))

    if len(sieve) < N - 1:
        return 0
    else:
        return list(sieve)[N - 1]


def main():
    primes(NN)
    primes2(NN)


zz = input('Введите что ищем - какое по счету простое число: ')
print(primes(zz))
print(primes2(zz))


# Замеры делались на "вычисление ряда чисел"
# print('1 : ', timeit.timeit('primes(zz)', number=10, globals=globals()))  # 0.46852359999999993
# print('2 : ', timeit.timeit('primes2(zz)', number=10, globals=globals()))  # 0.19654269999999996

# cProfile.run('main()')

'''
ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.380    0.380 <string>:1(<module>)
        1    0.262    0.262    0.266    0.266 L4-prime.py:13(primes)
        1    0.109    0.109    0.109    0.109 L4-prime.py:35(primes2)
        1    0.005    0.005    0.380    0.380 L4-prime.py:46(main)
        1    0.000    0.000    0.380    0.380 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method math.sqrt}
    41538    0.004    0.000    0.004    0.000 {method 'append' of 'list' objects}

'''

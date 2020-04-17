'''

Нахождение простых чисел
'''

import timeit
import cProfile
import math
NN = 500000

# Алгоритм - тупарь. Пройдемся, просеим. Без затей.
def primes(n):
    a =[0]+ list(range(1, n))
    a[1] = 0

    m = 1
    while m < n:  # перебор всех элементов до заданного числа
        if a[m] != 0:  # если он не равен нулю, то
            j = m * 2  # увеличить в два раза (текущий элемент простое число)
            while j < n:
                a[j] = 0  # заменить на 0
                j = j + m  # перейти в позицию на m больше
        m += 1

    b = []
    for i in a:
        if a[i] != 0:
            b.append(a[i])

    return b


# идея в вычитании множеств - 2ек умнорженных и т.д..
def primes2(N):
    """Возвращает все простые от 2 до N"""
    sieve = set(range(2, N))
    for i in range(2, int(math.sqrt(N))):
        if i in sieve:
            sieve -= set(range(2 * i, N, i))
    return sieve




def main():
    primes(NN)
    primes2(NN)


#print(primes(NN))
#print(primes2(NN))

#print('1 : ', timeit.timeit('primes(NN)',  number=10, globals=globals()))  # 0.46852359999999993
#print('2 : ', timeit.timeit('primes2(NN)', number=10, globals=globals()))  # 0.19654269999999996

cProfile.run('main()')

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
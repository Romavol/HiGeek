'''
Переделка -
4 Определить, какое число в массиве встречается чаще всего.
'''

import random
import timeit
import cProfile

SIZE = 5000  ## БОЛЬШЕ 5 тыс 2й алгоритм положит машину. Осторожно !
MIN_ITEM = 1
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]


# print(array)



def chan1():  # мой вариант
    res = dict((array.count(i), i) for i in set(array))
    max_ = 1
    num_ = 1

    for key, value in res.items():
        if key > num_:
            num_ = key
            max_ = value


def chan2():
    num = array[0]
    frequency = 1
    for i in range(len(array)):
        spam = 1
        for j in range(i + 1, len(array)):
            if array[i] == array[j]:
                spam += 1
        if spam > frequency:
            frequency = spam
            num = array[i]

def chan4():  # оптимизированный вариант 2го
    num = array[0]
    frequency = 1
    len_= len(array)
    for i in range(len_):
        spam = 1
        for j in range(i + 1, len_):
            if array[i] == array[j]:
                spam += 1
        if spam > frequency:
            frequency = spam
            num = array[i]


def chan3():
    counter = {}
    frequency = 1
    num = None
    for item in array:
        if item in counter:
            counter[item] += 1
        else:
            counter[item] = 1

        if counter[item] > frequency:
            frequency = counter[item]
            num = item


# print('1 : ', timeit.timeit('chan1()', number=10, globals=globals()))  #  0.0638158
# print('2 : ', timeit.timeit('chan2()', number=10, globals=globals()))  # 16.681424
# print('3 : ', timeit.timeit('chan3()', number=10, globals=globals()))  #  0.006683799999997575
# print('4 : ', timeit.timeit('chan4()', number=10, globals=globals()))  # 15.834107


def main():
    chan1()
    chan2()
    chan3()



cProfile.run('main()')

'''
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      101    0.000    0.000    0.013    0.000 L4-t2.py:21(<genexpr>)
        1    6.364    6.364    6.366    6.366 L4-t2.py:31(chan2)
        1    0.002    0.002    0.002    0.002 L4-t2.py:44(chan3)
        1    0.000    0.000    6.380    6.380 L4-t2.py:64(main)
        1    0.000    0.000    6.381    6.381 {built-in method builtins.exec}
    10001    0.002    0.000    0.002    0.000 {built-in method builtins.len}   # вот  что оптимизил в 4м, мелоч конечно
      100    0.013    0.000    0.013    0.000 {method 'count' of 'list' objects}

Выводы - вложенные циклы опасны. Пока видно что встроенные функции огонь, но говноалгоритмом можно все испортить.


'''

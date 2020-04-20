'''
Переделка -
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
'''

import random
import timeit
import cProfile

SIZE = 500000
MIN_ITEM = 1
MAX_ITEM = 200
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]


# print(array)


def chan3():
    # попробуем скакать по массиву с краев как Pacman
    # Худший алгоритм.

    MIN_ITE = float('inf')  # мы какбы не знаем самого большого числа.
    MAX_ITE = float('-inf')
    fromstart = 0
    fromend = SIZE - 1
    while fromstart <= fromend:

        for i in (fromstart, fromend):
            if array[i] < MIN_ITE:
                MIN_ITE = array[i]
                ind_min = i
            if array[i] > MAX_ITE:
                MAX_ITE = array[i]
                ind_max = i
        fromend -= 1
        fromstart += 1

    # print(f'Заменены : min поз {ind_min} (число {MIN_ITE} ) на max поз {ind_max}(число {MAX_ITE}) ')

#  for i in (fromstart, fromend):
def chan1():
    MIN_ITE = float('inf')  # мы какбы не знаем самого большого числа.
    MAX_ITE = float('-inf')
    for no, i in enumerate(array):
        if i < MIN_ITE:
            MIN_ITE = i
            ind_min = no
        if i > MAX_ITE:
            MAX_ITE = i
            ind_max = no
    array[ind_max], array[ind_min] = array[ind_min], array[ind_max]


#  print(f'Заменены : min поз {ind_min} (число {MIN_ITE} ) на max поз {ind_max}(число {MAX_ITE}) ')


def chan2():
    # 2 вариант как пример асимптотической сложности
    # O(n) против O(n) * (1 + 1 + 0.5 + 0.5)
    min_num = min(array)
    max_num = max(array)
    idx_min = array.index(min_num)
    idx_max = array.index(max_num)
    array[idx_min], array[idx_max] = array[idx_max], array[idx_min]


# print(f'2 : min поз {idx_min}  - -  {idx_max}')


print('1: ', timeit.timeit('chan1()', number=100, globals=globals()))  # 4.1140612
print('2 : ', timeit.timeit('chan2()', number=100, globals=globals()))  # 1.5630628
print('3 : ', timeit.timeit('chan3()', number=100, globals=globals()))  # 11.1437147


def main():
    chan1()
    chan2()
    chan3()


# cProfile.run('main()')
'''
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.340    0.340    0.340    0.340 L4-t1.py:19(chan3)     # Ну тут ожидаемы провал дурацкого алгоритма
        1    0.127    0.127    0.127    0.127 L4-t1.py:41(chan1)
        1    0.000    0.000    0.047    0.047 L4-t1.py:57(chan2)
        1    0.000    0.000    0.514    0.514 L4-t1.py:75(main)

Выводы - возможно метод while прямо медленней, или скакать по массиву - не очень. 
хотя непонятно что я там так медленно сделал.


'''

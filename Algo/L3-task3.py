'''
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
'''

import random

SIZE = 100000
MIN_ITEM = 1
MAX_ITEM = 200
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

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
print(f'Заменены : min поз {ind_min} (число {MIN_ITE} ) на max поз {ind_max}(число {MAX_ITE}) ')
print(array)

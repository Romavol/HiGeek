'''
В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой
 (оба являться минимальными), так и различаться.
'''

import random

SIZE = 40
MIN_ITEM = 1
MAX_ITEM = 400
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

min1 = 100000000000000000


for i in array:
    if i < min1:
        min2 = min1
        min1 = i
    elif i <= min2:
        min2 = i
print(f' Самое малое = {min1} а 2е наименьшее = {min2}')

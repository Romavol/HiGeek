'''
Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями 8, 3,
 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля), т.к. именно в этих
  позициях первого массива стоят четные числа.
'''
import random

SIZE = 100
MIN_ITEM = 1
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

even_ = []
for no, i in enumerate(array):
    if not i % 2:
        even_.append(no)
print('Четные позиции :')
print(*even_,)

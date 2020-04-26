'''
Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
 Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые
 не меньше медианы, в другой — не больше медианы.

import random

array = [i for i in range(10)]
print(array)
random.shuffle(array)
print(array)

'''


def sort3n(arr):
    idx = 0
    while idx < len(arr):
        if idx == 0:
            idx = idx + 1
        if arr[idx] >= arr[idx - 1]:
            idx = idx + 1
        else:
            arr[idx], arr[idx - 1] = arr[idx - 1], arr[idx]
            idx = idx - 1
    return arr


arr = [55, 22, 11, 3, 4, 7, 2, 2, 1, 6, 9]
sort3n(arr)

print(arr)
print(f'Медиана от гномов = {arr[(len(arr) // 2)]}')

# не сортировками найти ниасилил.
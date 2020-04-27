'''
2). Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на
 промежутке [0; 50). Выведите на экран исходный и отсортированный массивы
'''

import numpy as np

def mergeSort(a, idxstart, idxlast):
    def merge(a, idxstart, split, idxlast):
        pos1 = idxstart
        pos2 = split + 1
        pos3 = 0
        temp = [i for i in range(idxlast - idxstart + 1)]
        while pos1 <= split and pos2 <= idxlast:
            if a[pos1] < a[pos2]:
                temp[pos3] = a[pos1]
                pos1 += 1
                pos3 += 1
            else:
                temp[pos3] = a[pos2]
                pos2 += 1
                pos3 += 1
        while pos2 <= idxlast:
            temp[pos3] = a[pos2]
            pos3 += 1
            pos2 += 1
        while pos1 <= split:
            temp[pos3] = a[pos1]
            pos3 += 1
            pos1 += 1
        a[idxstart:idxlast + 1] = temp
        del (temp)

    if idxstart < idxlast:
        split = (idxstart + idxlast) // 2
        mergeSort(a, idxstart, split)
        mergeSort(a, split + 1, idxlast)
        merge(a, idxstart, split, idxlast)


array = np.random.uniform(0.1, 50, size=30)
print(array)
mergeSort(array, 0, (len(array) - 1))
print(array)

# тщательно проверенный интернет код. Сам не додумываюсь.

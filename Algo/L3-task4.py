'''
4 Определить, какое число в массиве встречается чаще всего.
'''

import random

SIZE = 3000
MIN_ITEM = 1
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

res = dict((array.count(i), i) for i in set(array))
max_ = 1
num_ = 1

for key, value in res.items():
    if key > num_:
        num_ = key
        max_ = value

print(num_, ' раз встречается число ', max_)

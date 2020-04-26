import sys
import random
import math
import platform

# - 1е пристрелочное задание и замеры
SIZE = 100
MIN_ITEM = 1
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
# print(array)

size1mem = sys.getsizeof(SIZE) + sys.getsizeof(MIN_ITEM) + \
           sys.getsizeof(MAX_ITEM) + sys.getsizeof(array)
# print(f'Вся до цикла = {size1mem=} ')

even_ = []
for no, i in enumerate(array):
    if not i % 2:
        even_.append(no)
size1mem += sys.getsizeof(even_) + sys.getsizeof(no) + sys.getsizeof(i)

print(f'Память 1 этапа = {size1mem=} ')  # итого 1 = 734

# Варианты поиска простых

# вариант 2

NN = 2000000

arra = [0] + list(range(1, NN))
arra[1] = 0
rezfind = 1
m = 1
while m < NN:
    spam = arra[m]
    if arra[m] != 0:
        if rezfind == NN:
            print(arra[m])
        else:
            rezfind += 1
        j = m * 2
        while j < NN:
            arra[j] = 0
            j = j + m
    m += 1
new_array = []
for i in arra:
    if arra[i] != 0:
        new_array.append(arra[i])

# print(sys.getsizeof(arra[-1]))
# print(len(arra))
size2mem = sys.getsizeof(NN) + sys.getsizeof(j) + sys.getsizeof(arra) + \
           sys.getsizeof(spam) + sys.getsizeof(new_array) + sys.getsizeof(m) + \
           sys.getsizeof(rezfind) + sys.getsizeof(arra[-1]) * (len(arra) + len(new_array))
print(f'Память 2 этапа = {size2mem=} ')  # итого 2 = 8660524 (new - 34447720)

# вариант 3

N = NN
sieve = set(range(2, NN))

for i in range(2, int(math.sqrt(NN))):
    if i in sieve:
        sieve -= set(range(2 * i, NN, i))

if len(sieve) < N - 1:
    spamlist = 0
else:
    spamlist = list(sieve)[N - 1]

for i in sieve:
    eggs = sys.getsizeof(i)
    break

# print(f'{id(N)=} , {id(NN)=} ') # 2 переменных одинаковые, считаю 1 раз
# print(f'{sys.getsizeof(sieve)=} {sys.getsizeof(NN)=} {sys.getsizeof(spamlist)=} ')
size3mem = (sys.getsizeof(NN) + sys.getsizeof(i) + sys.getsizeof(sieve) + sys.getsizeof(spamlist)
            + eggs * len(sieve))
print(f'Память 3 этапа = {size3mem=} ')  # итого 3 = 16777366 (16мБ) (а правильно 18862428 )
print(platform.architecture())  # ('32bit', 'WindowsPE')

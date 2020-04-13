# НЕ ДОДЕЛАНО !
class Matrix:
    def __init__(self, parlist):
        self.matrix_l = parlist

    def __str__(self):
        return 'Matrix : \n' + '\n'.join(['\t'.join(map(str, line)) for line in self.matrix_l])

    def __add__(self, other):
        return list(map(lambda x, y: list(map(lambda z, w: z + w, x,y)), self.matrix_l, other))


lista = [1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 22, 12]
listb = [7, 8, 9], [9, 8, 7], [1, 2, 3], [2, 2, 2]

ma_a = Matrix(lista)
ma_b = Matrix(listb)
summ = ma_a + ma_b
ma_result = summ
print(ma_result)

# ---------------- 2

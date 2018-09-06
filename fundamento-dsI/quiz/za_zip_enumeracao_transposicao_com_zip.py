'''
Quiz: Transposição com zip
Use zip para transpor data de uma matriz 4 por 3 para uma matriz 3 por 4. Na verdade, existe um truque legal para isso!
Fique à vontade para olhar para as soluções, caso não consiga descobrir.
'''

data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))
print(data)

data_transpose = tuple(zip(*data))
print(data_transpose)
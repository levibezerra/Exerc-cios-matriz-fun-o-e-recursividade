maior_valor = 0
matriz = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        if i != j:
            if matriz[i][j] > maior_valor:
                maior_valor = matriz[i][j]
print(f'O maior valor é {maior_valor}')
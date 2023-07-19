matriz = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
soma = 0
itens = 0
for i in range(len(matriz)):
    soma += matriz[i][len(matriz) - i - 1]
    itens += 1
media = soma / itens
print(f'A media da diagonal secundaria é: {media}')
A = []
B = []
resultado = []
print('Digite os numeros da matriz A.')
for i in range(3):
    linha = []
    for j in range(3):
        num1 = int(input(f'Digite o numero da posição [{i}][{j}]: '))
        linha.append(num1)
    A.append(linha)
print('Digite os numeros da matriz B.')
for i in range(3):
    linha = []
    for j in range(3):
        num2 = int(input(f'Digite o numero da posição [{i}][{j}]: '))
        linha.append(num2)
    B.append(linha)
for i in range(3):
    linha = []
    for j in range(3):
        soma = A[i][j] + B[i][j]
        linha.append(soma)
    resultado.append(linha)
print('A matriz da soma de A + B é:')
for linha in resultado:
    print(linha)
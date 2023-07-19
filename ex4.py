A = []
B = []
C = []
print('Digite os números da matriz A.')
for i in range(3):
    linha = []
    for j in range(3):
        num1 = int(input(f'Digite o número da posição: [{i}][{j}]: '))
        linha.append(num1)
    A.append(linha)
print('Digite os números da matriz B.')
for i in range(3):
    linha = []
    for j in range(3):
        num2 = int(input(f'Digite o número da posição: [{i}][{j}]: '))
        linha.append(num2)
    B.append(linha)
for i in range(3):
    linha = []
    for j in range(3):
        mult = A[i][j] * B[i][j]
        linha.append(mult)
    C.append(linha)
print('A matriz da multiplicação de A * B é:')
for linha in C:
    print(linha)
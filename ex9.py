def fib(x):
    if x == 0 or x == 1:
        return x
    else:
        return fib(x - 1) + fib(x - 2)
posicao = int(input('Digite um número para posição: '))
valor = fib(posicao)
print(f'O valor da posição {posicao} é: {valor}')
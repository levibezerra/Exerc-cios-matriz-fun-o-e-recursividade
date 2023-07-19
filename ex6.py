num = int(input("Digite um número inteiro: "))
def numero_primo(x):
    divisor = 0
    for c in range(1, num+1):
        if(num % c == 0):
            divisor += 1
    if(divisor == 2):
        return True
    else:
        return False
print(f'O número {num} é primo: {numero_primo(num)}')
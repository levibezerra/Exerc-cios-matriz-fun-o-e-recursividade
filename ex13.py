def soma(num):
    if num == '':
        return 0
    else:
        return int(num[0]) + soma(num[1:])
d = str(input('Digite um numero: '))
var = soma(d)
print(f'A soma do número é: {var}')
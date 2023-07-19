def letra(palavra):
    if palavra == '':
        return 0
    else:
        return 1 + letra(palavra[1:])
l = str(input('Digite uma palavra: '))
var = letra(l)
print(f'A palavra tem {var} letras')
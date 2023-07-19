def cont_a(palavra):
    if palavra == '':
        return 0
    else:
        cont = 0
        if palavra[0] == 'A':
            cont += 1
        return cont + cont_a(palavra[1:])
p = str(input('Digite uma palavra: ')).upper()
var = cont_a(p)
print(f'A palavra {p} tem {var} A.')
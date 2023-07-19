def concatena(lista):
    if len(lista) == 0:
        return ''
    else:
        return lista[0] + concatena(lista[1:])
lista = []
c = int(input('Informe o tamanho da lista: '))
for i in range(c):
    t = str(input('Digite as letras para a lista: '))
    lista.append(t)
var = concatena(lista)
print(var)
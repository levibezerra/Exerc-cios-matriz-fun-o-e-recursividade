def inverter_palavra():
    palavra = input('Informe uma palavra com mais de 4 caracteres: ')
    while len(palavra) < 4:
        print('A palavra não atingiu o tamanho mínimo necessário!')
        palavra = input('Informe uma palavra com mais de 4 caracteres: ')
    return palavra[::-1]
nome = inverter_palavra()
print(nome)

def primeira_metade():
    palavra = input('Informe uma palavra com mais de 4 caracteres: ')
    while len(palavra) < 4:
        print('A palavra não atingiu o tamanho mínimo necessário!')
        palavra = input('Informe uma palavra com mais de 4 caracteres: ')
    meta = int(len(palavra) / 2)
    return palavra[0:meta:1]
nome = primeira_metade()
print(nome)
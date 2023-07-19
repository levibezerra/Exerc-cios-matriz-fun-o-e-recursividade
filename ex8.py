def concatenar_palavra():
    f = ''
    palavra = input('Informe uma palavra com mais de 4 caracteres: ')
    while len(palavra) < 4:
        print('A palavra não atingiu o tamanho mínimo necessário!')
        palavra = input('Informe uma palavra com mais de 4 caracteres: ')
    meta = int(len(palavra) / 2)
    meta_final = []
    meta_comeco = []
    for i in palavra[0:meta:1]:
        meta_comeco.append(i)
    for i in palavra[meta:len(palavra):1]:
        meta_final.append(i)
    while len(meta_final) > 0:
        if len(meta_comeco) > 0:
            letra1 = meta_comeco[0]
            meta_comeco.pop(0)
            f += letra1
        meta2 = meta_final[0]
        meta_final.pop(0)
        f += meta2
    return f
resultado = concatenar_palavra()
print(resultado)
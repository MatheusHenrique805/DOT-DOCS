'''16) Ler uma lista X de 10 elementos inteiros e positivos. Criar uma lista Y da seguinte forma: os elementos de Y com índice par receberão os respectivos elementos de X divididos por 2; os elementos com índice ímpar receberão os respectivos elementos de X multiplicados por 3. Escrever as listas X e Y.'''
def criar_listay(listax):
    listay = []
    for elemento in listax:
        if listax.index(elemento) % 2 == 0:
            elemento = listax[listax.index(elemento)] / 2
            listay.append(elemento)
        else:
            elemento = listax[listax.index(elemento)] * 3
            listay.append(elemento)
            
    return listay
def main():
    while True:
        try:
            listax = []
            for i in range(10):
                elemento = int(input(F'Digite o {i+1}º número INTEIRO POSITIVO da lista X.\n'))
                if elemento >= 0:
                    listax.append(elemento)
                else:
                    raise ValueError
            
            listay = criar_listay(listax)

            print(f'lista X e Y, respectivamente:\n{listax}\n{listay}')
            break
        except ValueError:
            print('ELEMENTO DIFERENTE DO ESPERADO!!')
if __name__ == '__main__':
    main()
'''18) Ler uma lista X de 10 elementos. A seguir copiar todos os valores negativos da lista X para uma lista R, sem      deixar elementos vazios entre os valores copiados. Escrever as listas X e R.'''
def criar_listar(listax):
    listar = []
    for valor in listax:
        if valor < 0:
            listar.append(valor)
        else:
            pass
    
    return listar


def main():
    while True:
        try:
            listax = []
            for i in range(10):
                        elemento = float(input(f'Digite o {i+1}º valor a entrar na lista X.\n'))
                        listax.append(elemento)
                        
            listar = criar_listar(listax)
            print(f'Lista X:\n{listax}\nLista R:\n{listar}')
            break
        except:
            print('INFORMAÇÃO DIFERENTE DO ESPERADO!!')
if __name__ == '__main__':
    main()
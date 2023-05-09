'''14) Ler uma lista C de 10 elementos inteiros, trocar todos os valores negativos da lista C por 0. Escrever a lista C modificada'''
def modificar_lista(lista):
    for elemento in lista:
        if elemento < 0:
            indice = lista.index(elemento)
            elemento = 0
            lista[indice] = elemento
        else:
            pass
    
    return lista


def main():
    while True:
        try:
            listac = []
            for i in range(10):
                elemento = int(input(f'Digite o {i+1}º número INTEIRO da lista.\n'))
                listac.append(elemento)
            
            listac_mod = modificar_lista(listac)
        
            print(f'{listac_mod}')
            break
        except:
            print('ELEMENTO INCORRETO PARA A LISTA!!')
            
if __name__ == '__main__':
    main()
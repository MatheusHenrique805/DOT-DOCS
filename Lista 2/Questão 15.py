'''15) Ler uma lista D de 10 elementos. Criar uma lista E, com todos os elementos de D na ordem inversa, ou seja, o último elemento passará a ser o primeiro, o penúltimo será o segundo e assim por diante. Escrever todo a lista D e todo a lista E.'''
def main():
    listad = []
    listae = []
    for i in range(10):
        elemento = input(f'Digite o {i+1}º elemento da lista,\n')
        listad.append(elemento)
        listae.append(elemento)

    listae.reverse()
    
    print(f'lista D:\n{listad}\nLista E:\n{listae}')
    
if __name__ == '__main__':
    main()
'''19) Ler duas listas: R de 5 elementos e S de 10 elementos. Gerar uma lista X de 15 elementos cujas 5 primeiras posições contenham os elementos de R e as 10 últimas posições, os elementos de S. Escrever a lista X.'''
def criar_lista(li_r):
    while True:
        try:
            lista = []
            for i in range(len(li_r)+5):
                elemento = int(input(f'Digite o {i+1}º número INTEIRO da lista S.\n'))
                lista.append(elemento)
            break
        except:
            print('DADO DIFERENTE DO ESPERADO!!')
    
    return lista   
def main():
    while True:
        try:
            lista_r = []
            for i in range(5):
                elemento = float(input(f'Digite o {i+1}º número DECIMAL da lista R.\n'))
                lista_r.append(elemento)
            
            lista_s = criar_lista(lista_r)
            listax = lista_r + lista_s
            
            print(f'A lista X:\n{listax}')
            break
        except:
            print('DADO DIFERENTE DO ESPERADO!!')
if __name__ == '__main__':
    main()
'''9) Dada uma lista X numérica contendo 5 elementos, fazer um programa que crie e exiba na tela uma lista Y. A lista Y deverá conter o mesmo  conteúdo da lista X na ordem inversa'''
def main():
    listax = []
    listay = []
    for i in range(5):
        elemento = input(f'Digite o {i+1}º elemento da lista,\n')
        listax.append(elemento)

    listax.reverse()
    listay = listax
    
    print(f'A lista Y com o conteúdo da lista X invertido:\n{listay}')
    
if __name__ == '__main__':
    main()
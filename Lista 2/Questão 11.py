'''11) Faça um programa que alimente uma lista com um número de posições definidas pelo usuário. Esta lista deverá armazenar um conjunto de nomes em diferentes posições. Crie um mecanismo para alimentar elementos da lista e pesquisar por um valor existente.
    ==== =MENU========
    1)Cadastar nome
    2)Pesquisar nome
    3)Listar todos os nome
    0) Sair do programa'''
def verifica_tamanho(string):
    if len(string) <= 4:
        while len(string) <= 4: 
            string = input('HAHAHAHA!!!Digita novamente.\n').capitalize()
    
        return string
    else:
        return string
            

def cadastra_nome(quant_nomes):
    lista = []
    for i in range(quant_nomes):
        nome = input(f'{i+1}º nome para cadastro:').capitalize()
        verifica_tamanho(nome)
        if nome.isalpha:
            sobrenome = input('Sobrenome:').capitalize()
            verifica_tamanho(sobrenome)
            if sobrenome.isalpha():
                nome = nome +' '+ sobrenome
                lista.append(nome)
            else:
                while not sobrenome.isalpha():
                    sobrenome = input('Encontramos um erro!!Digite novamente o sobrenome.\n').capitalize()
                    verifica_tamanho(nome)
                    
                nome += +' '+ sobrenome
                lista.append(nome)
        else:
            while not nome.isalpha():
                nome = input('Encontramos um erro!!Digite novamente o nome.\n').capitalize()
                verifica_tamanho(nome)
                
            sobrenome = input('Sobrenome:')
            if sobrenome.isalpha():
                nome += +' '+ sobrenome
                lista.append(nome)
            else:
                while not sobrenome.isalpha():
                    sobrenome = input('Encontramos um erro!!Digite novamente o sobrenome.\n').capitalize()
                    verifica_tamanho(sobrenome)
                nome += +' '+ sobrenome
                lista.append(nome)
    
    return lista


def pesquisar_nome(lista, nom):
    retorno = 'Nome não cadastrado'
    for nome in lista:
        if nome == nom:
            retorno = nome
            break
        else:
            continue
    
    return retorno


def listar_nomes(lista):
    for nome in lista:
        return nome
    

def main():
    lista_nomes = []
    while True:
        try:
            while True:
                print('='*6+'MENU'+'='*6+'\n1)Cadastar nome\n2)Pesquisar nome\n3)Listar todos os nome\n0) Sair do programa')
                escolha = int(input('Digite o número correspondente a ação desejada.\n'))
                if escolha == 1:
                    quant_nomes = int(input('Digite a quantidade de nomes que vão ser cadastrados.\n'))
                    lista_nomes = cadastra_nome(quant_nomes)
                elif escolha == 2:
                    nome = input('Digiite com ATENÇÃO seu nome e sobrenome.\n').capitalize() 
                    print(pesquisar_nome(lista_nomes))
                elif escolha == 3:
                    
                    print(listar_nomes(lista_nomes, nome))
                elif escolha == 0:
                    break
                else:
                    print('Não encontramos ações para esse valor!!Digite novamento.\n')
            break
        except:
            print('NÃO ENCONTRAMOS ESSA AÇÃO!!!1')
        
            
if __name__ == '__main__':
    main()
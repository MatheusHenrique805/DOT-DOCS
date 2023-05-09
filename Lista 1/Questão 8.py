'''Q8. Escreva uma função que lê um caractere digitado pelo usuário e retorna este caractere somente se ele for igual a 'S' ou 'N'. Se o caractere não for nem 'S' nem 'N', a função imprime a mensagem 'Caractere inválido. Digite novamente'. Use esta função em um programa que fica lendo do usuário um número qualquer e imprime este número ao cubo na tela. O programa deve ficar lendo os números até o usuário responder 'N' à pergunta se ele deseja continuar ou não.'''

def ler_caractere(char):
    
    char = input('Deseja continuar.? S para Sim N para Não.\n').upper()[0]
    
    if char == 'S' or char == 'N':
        pass
    else:
        while char != 'S':
            char = input('Caractere inválido. Digite novamente.\n').upper()[0]
           
   
    return char


def main():
    
        try:
            letra = 'S'
            
            while letra == 'S':
                
                num = int(input('Digite um número INTEIRO.\n'))
                if num == 0:
                    num = 1
                    print(f'{num ** 3}')
                    letra = ler_caractere(letra)
                else:
                    print(f'{num ** 3}')
                    letra = ler_caractere(letra)
                 
                    
        except ValueError:
            print('Não digite nada diferente do que foi requisitado')
            main()

if __name__ == '__main__':
    main()
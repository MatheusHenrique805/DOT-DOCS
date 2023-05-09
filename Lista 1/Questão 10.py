'''Q10. Escreva um programa composto de uma função Max e o programa principal como segue:
a) A função Max recebe como parâmetros de entrada dois números inteiros e retorna o maior. Se forem iguais retorna qualquer um deles;
b) O programa principal lê 4 séries de 4 números a, b. Para cada série lida imprime o maior dos quatro números usando a função Max.'''

def Max(a, b, c, d):
    
    n_max = 0
    
    if a <= d:
        a, d = d, a    
    if a <= c:
        a, c = c, a
    if a <= b:
        a, b = b, a
    if b <= d:
        b, d = d, b
    if b <= c:
        b, c = c, b
    if c <= d:
        c, d = d, c
        n_max = a
    else:
        n_max = a
        
    
    return n_max


def main():

    executa = True
    while executa:
        try:
            for i in range(4):
                a = int(input(f'Digite o 1º número INTEIRO da {i + 1}ª série.\n'))
                b = int(input(f'Digite o 2º número INTEIRO da {i + 1}ª série.\n'))
                c = int(input(f'Digite o 3º número INTEIRO da {i + 1}ª série.\n'))
                d = int(input(f'Digite o  4º e último número INTEIRO da {i + 1}ª série.\n'))
                num_maximo= Max(a, b, c, d)
                print(f'O maior número da {i + 1}ª série é {num_maximo}') 
            break
        except ValueError:
            print('Por favor, não torne esse processo frustrante!')
            print('Exemplos de número inteiro: 1, 2 , 3, 4')
            
        
if __name__ == '__main__':
    main()
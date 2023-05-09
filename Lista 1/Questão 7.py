'''Q7. Faça um programa para calcular o Fatorial de um número. Para o cálculo do fatorial, sabemos que N! depende de (N-1)!; este por sua vez depende de (N-2)!; e, assim por diante, até que N seja 1, quando então tem-se que fatorial de 1 é igual a 1 mesmo. Utilize uma função que recebe como parâmetro de entrada o número a ser calculado o fatorial, do tipo inteiro, e retorna o fatorial deste número, também do tipo inteiro.'''

def num_fatorial(n):
    p = fator = 1
    
    if n != 0:
        while p < n:
            p += 1
            fator *= p
    else:
        pass
        
    
    return fator
        

def main():
    
    executa = True
    
    while executa:
        try:
            num = int(input(f'Qual número quer fatorar?\n'))
            
            fatorial = num_fatorial(num)

            print(f'{num}! = {fatorial}')
            break
        except ValueError:
            print('Digite apenas um número INTEIROS!')
            

if __name__ == '__main__':
    main()
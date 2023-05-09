'''Q9. Escreva uma função que recebe 2 números inteiros n1 e n2 como entrada e retorna a soma de todos os números inteiros contidos no intervalo [n1,n2]. Use esta função em um programa que lê n1 e n2 do usuário e imprime a soma.'''

def somar_intervalo(n1, n2):
    
    soma = 0
    
    if n1 < n2:
        for i in range(n1 + 1, n2):
            soma += i
    elif n1 > n2:
        for i in range(n2 + 1, n1):
            soma += i
    else:
        pass
    
    return soma


def main():
    executa = True
    
    while executa:
        try:
            num1 = int(input('Digite um número INTEIRO qualquer.\n'))
            num2 = int(input('Digite outro número inteiro.\n'))
            
            soma = somar_intervalo(num1, num2)
            
            print(f'A soma dos número entre {num1} e {num2} é {soma}')
            break
        except ValueError:
            print('Digite apenas o que se pede, UM NÚMERO INTEIRO(1, 2, 3, 4, ec).') 
            
if __name__ == '__main__':
    main() 
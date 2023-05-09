'''Q15. Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S.
        S = 2/4 + 5/5 + 10/6 + 17/7 + 26/8 + ... +(N^2+1)/(N+3)'''
def calcular(n):
    s = 0
    for i in range(1, n + 1):
        s  += (i ** 2 + 1) / (i + 3)

    return s

    
def main():
    while True:
        try:
            n = int(input('Digite apenas um número INTEIRO e MAIOR QUE ZERO.\n'))
            if n > 0:
                s = calcular(n)
                print(f'\nQuando N é {n}, S é {s:.1f}.')
            else:
                raise ValueError
            break
        except ValueError:
            print('Houve um erro com o dado fornecido. Digite novamente!')
if __name__ == '__main__':
    main()
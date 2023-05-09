'''Q13. Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S. S = 1 + ½ + 1/3 + ¼ + 1/5 + 1/N.'''
def calculo(n):
    s = 0
    for i in range(1, n + 1):
        s += 1/i
    
    return s
    
def main():
    while True:
        try:
            n = int(input('Digite apenas um número INTEIRO e MAIOR QUE ZERO.\n'))
            if n > 0:
                s = calculo(n)
                print(f'\nQuando N é {n}, S é {s:.1f}.')
            else:
                raise ValueError
            break
        except ValueError:
            print('Enquanto você errar ficaremos nesse loop!')

if __name__ == '__main__':
    main()
        
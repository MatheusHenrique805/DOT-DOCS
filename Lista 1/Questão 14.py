'''Q14. Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S. 
        S = 1 + 1/1! + ½! + 1/3! + 1 /N!'''
def fatorar(indice):
    fatoração = 1

    for i in range(1, indice + 1):
        fatoração *= i
        
    return fatoração

def calcular(n):
    s = 0
    for i in range(1, n + 1):
        s += 1/fatorar(i)
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
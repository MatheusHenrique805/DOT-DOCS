'''Q11. Faça uma função que recebe, por parâmetro, um valor inteiro e positivo e retorna o número de divisores desse valor.'''
def divisores(n):
    contador = 0
    
    for i in range(1, n + 1):
        if n % i == 0:
            contador += 1
        else:
            pass 
    
    return contador


def main():
    while True:
        try:
            num = int(input('Digite um número INTEIRO e MAIOR QUE 0.\n'))
            if num > 0:
                contagem = divisores(num)
                print(f'\n{num} têm {contagem} divisores.')
            else:
                raise ValueError
            break
        except ValueError:
            print('Digite apenas o que se pede!')
    
if __name__ == '__main__':
    main()
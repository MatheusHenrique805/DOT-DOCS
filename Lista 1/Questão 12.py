'''Q12. Escreva uma função que recebe, por parâmetro, um valor inteiro e positivo e retorna o somatório desse valor'''
def soma(n):
    acumulador = 0
    for i in range(1, n + 1):
        acumulador += i
    
    return acumulador        

def main():
    while True:
        try:
            num = int(input('Digite apenas um número INTEIRO e MAIOR QUE ZERO.\n'))
            if num >= 0:
                somatorio = soma(num)
                print(f'\nO somatório de {num} é {somatorio}.')
            else:
                raise ValueError    
            break
        except ValueError:
            print('Evite digitar letras, acentuações, númeração com pontos e números negativos')
            
if __name__ == '__main__':
    main()
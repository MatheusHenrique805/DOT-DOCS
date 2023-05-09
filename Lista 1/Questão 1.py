'''Q1. Faça uma função que recebe um número inteiro por parâmetro e retorna verdadeiro se ele for par e falso se for ímpar.'''

def par_impar(num):
    resp = f''
    
    if num % 2 == 0:
        resp = f'Verdadeiro'
    else:
        resp = f'Falso'

    return resp

def main():
    
    keep_going = True
    
    while keep_going:
        try:
            num = int(input('Digite um número inteiro.\n'))
            
            resposta = par_impar(num)
                
            print(f'{num} é {resposta}.\nVerdadeiro = par, Falso = ímpar.')
            break
        except ValueError:
            print('Digite apenas o que se pede')

if __name__ == '__main__':
    main()
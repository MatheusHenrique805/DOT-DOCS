'''Q2. Escreva um programa que leia o raio de um círculo e faça duas funções: uma função chamada área que calcula e retorna a área do círculo e outra função chamada perímetro que calcula e retorna o perímetro do círculo.
        Área = PI * r2; Perímetro = PI * 2 * r;'''

def perimetro(r):
    return 2 * 3,14 * r


def area(r):
    return 3,14 * r ** 2


def main():
    
    keep_going = True
    
    while keep_going:
        try:
            raio = float(input('Quanto mede o raio do círculo?\n'))
            
            PdC = perimetro(raio)
            AdC = area(raio)
            
            print(f'O perímetro e a área desse círculo são de, respectivamente,{PdC:.2f} m e {AdC:.2f} m². ')
            break
        except ValueError:
            print('Digite somente o valor do raio, sem métrica')
    
if __name__ == '__main__':
    main()
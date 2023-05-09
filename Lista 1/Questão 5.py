'''Q5. Faça um programa que leia a altura e o sexo (codificado da seguinte forma: 1:feminino 2:masculino) de uma pessoa. Depois faça uma função chamada peso ideal que receba a altura e o sexo via parâmetro e que calcule e retorne seu peso ideal, utilizando as seguintes fórmulas:
        - para homens : (72.7 * h) – 58
        - para mulheres : (62.1 * h) – 44.7
        Observação: Altura = h (na fórmula acima).'''

def peso_ideal(h, s):
    p_i = 0
    if s == 1:
        p_i = (62.1 * h) - 44.7
    elif s == 2:
        p_i = (72.7 * h) - 58
    else:
        raise ValueError
    
    return p_i

def main():
    
    keep_going = True
    while keep_going:
        try:
            altura = float(input('Qual é a sua altura?\n'))
            sexo = int(input('Informe seu sexo. 1 para feminino e 2 para masculino\n'))
            
            pes_ideal = peso_ideal(altura, sexo)
            
            print(f'O seu peso ideal é de {pes_ideal:.1f} kg')
            break
        except ValueError:
            print('Digite somente com números e ponto, e opções válidas')
            
        
if __name__ == '__main__':
    main()
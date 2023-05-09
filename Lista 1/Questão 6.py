'''Q6. Escreva um programa para ler o número de lados de um polígono regular e a medida do lado (em cm). Faça um procedimento que receba como parâmetro o número de lados e a medida do lado deste polígono e calcule e imprima o seguinte:
        - Se o número de lados for igual a 3, escrever TRIÂNGULO e o valor do seu perímetro.
        - Se o número de lados for igual a 4, escrever QUADRADO e o valor da sua área.
        - Se o número de lados for igual a 5, escrever PENTÁGONO.
        Observação: Considere que o usuário só informará os valores 3, 4 ou 5.'''

def denominar_poligono(qtd_l, med_l):
    
    per_tri = qtd_l * med_l
    area_quadra = med_l ** 2
    nome =  f''
    
    if qtd_l == 3:
        nome = f'TRIÂNGULO com {per_tri:.1f} cm de perímetro'
    elif qtd_l == 4:
        nome = f'QUADRADO com {area_quadra} cm² de área'
    elif qtd_l == 5:
        nome = f'PENTÁGONO'
    else:
        raise ValueError
        
    return nome

   
def main():
    
    executando = True
    while executando:
        try:     
            qtd_lados = int(input('Quantos lados tem o polígono ?\n'))
                
            med_lado = float(input('Quanto mede o lado desse polígono em cm ?  Digite apenas o valor\n'))
            
            nome_poli = denominar_poligono(qtd_lados, med_lado)
            
            print(f'O seu polígono é um {nome_poli}')
            break
        except ValueError:
            print('Seu polígono ainda não foi mapeado ou ocorreu um erro na digitação')
        

if __name__ == '__main__':
    main()
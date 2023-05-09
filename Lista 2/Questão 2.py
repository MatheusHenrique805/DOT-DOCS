'''2) Faça um programa que grave uma lista com dez números reais, calcule e mostre a quantidade de números negativos e a soma dos números positivos dessa lista.'''
def calcular(lista):
    somapos = quantneg = 0 
    for i in range(len(lista)):
        if lista[i] >= 0:
            somapos += lista[i]
        else:
            quantneg += 1
    
    return somapos, quantneg
            
        
def main():
    while True:
        try:
            listanums = []
            print('Peço que só digite 10 NÚMEROS(+/-) para preencher uma lista, NÃO DIGITE NADA DIFERENTE DISSO!!!!')
            for i in range(10):
                i = float(input(f'Digite {i + 1}º número da lista.\n'))
                num = i
                listanums.append(num)
            
            soma_pos, quant_negat = calcular(listanums)
            
            print(f'A soma dos números positivos existentes na lista é {soma_pos}')
            print(f'e a quantidade de números negativos é {quant_negat}')
            break     
        except:
            print('Somente números posivitos ou negativos podem entrar na lista!!! Vai ter que começar denovo :(')

if __name__  == '__main__':
    main()
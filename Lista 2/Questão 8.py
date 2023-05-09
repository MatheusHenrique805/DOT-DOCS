'''8) Dada uma lista contendo letras do alfabeto, elabore um programa para verificar quantas vezes ocorreu a letra "A".
    OBS: Fazer crítica na entrada do caractere para aceitar somente letras.'''
def verificar_letraA(lista):
    contador = 0
    for letra in lista:
        if letra == 'A':
            contador += 1
        else:
            pass
    
    return contador
    
def main():
    while True:
        try:
            listaalfa = []
            for i in range(3):
                letra = input(f'Digite o {i+1}º caractere ALFABÉTICO da lista.\n').upper()[0]
                if letra.isalpha():
                    listaalfa.append(letra)
                else:
                    raise ValueError
                    
            contagem = verificar_letraA(listaalfa)
            
            print(f'A letra "A" ocorre {contagem} vezes na lista criada.')
            break
        except ValueError:
            print('O QUE SE PEDE SÃO LETRAS DO ALFABETOS!!!') 
if __name__ == '__main__':
    main()
    
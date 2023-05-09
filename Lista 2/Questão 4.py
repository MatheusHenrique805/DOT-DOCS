'''4) Faça um programa que grave uma lista com 15 posições, calcule e mostre:
    a) O maior elemento da lista e em que posição esse elemento se encontra;
    b) O menor elemento da lista e em que posição esse elemento se encontra.'''

def identificador(l): 
    
    return  max(l), min(l), l.index(max(l)), l.index(min(l))


def main():
    while True:
        try:
            listanums = []
            for i in range(15):
                num = float(input(f'Digite o {i+1}º número da lista.\n'))
                listanums.append(num)
                
            maiornum, menornum, imaior, imenor = identificador(listanums)
            
            print(f'O maior número da lista é {maiornum} e ele se encontra na {imaior + 1}ª posição')
            print(f'O menor número da lista é {menornum} e ele se encontra na {imenor + 1}ª posição')
            break
        except:
            print('NÃO ERRE!!! Isso pode ser frustrante!!')
        
if __name__ == '__main__':
    main()
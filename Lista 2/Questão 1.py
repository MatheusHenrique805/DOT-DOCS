
'''1) Faça um programa que grave uma lista de 100 elementos numéricos inteiros e:
    a) Mostre a quantidade de números pares;
    b) Grave uma lista somente com os números pares e mostre a lista;
    c) Mostre a quantidade de números ímpares;
    d) Grave uma lista somente com os números ímpares e mostre a lista.'''
from random import randint

def agrupar_num():
    listp = listi = []
    
    for i in range(100):
        i = randint(0, 999)
        if i % 2 == 0:
            listp.append(i)
        else:
            listi.append(i)
            
    
    return  listp, listi
        

def main():

    listpar, listimpar = agrupar_num()
    
    print(f'{len(listpar)} números pares\n{listpar}')
    print(f'{len(listimpar)} números ímpares\n{listimpar}')
    
if __name__ == '__main__':
    main()
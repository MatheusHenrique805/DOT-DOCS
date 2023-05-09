'''5) Faça um programa que leia duas listas de 10 elementos numéricos cada um e intercale os elementos deste em uma outra lista de 20 elementos'''
def preencher_lista(la, lb):
    lc = []
    for i in range(len(la)):
        lc.append(la[i])
        lc.append(lb[i])
                
    return lc


def ler_listaB():
    while True:
        try:
            lb = []
            for i in range(10):
               num = float(input(f'Digite {i+1}º número da lista B.\n'))
               lb.append(num)
            break
        except:
            print('Somente ELEMENTOS NÚMÉRICOS!!!')
    
    return lb 


def ler_listaA():
    while True:
        try:
            la = []
            for i in range(10):
               num = float(input(f'Digite {i+1}º número da lista A.\n'))
               la.append(num)
            break
        except:
            print('Somente ELEMENTOS NÚMÉRICOS!!!')
    
    return la        


def main():
    listaA = ler_listaA()     
    listaB = ler_listaB()
    listaC = preencher_lista(listaA, listaB)

    print(f'Esse foi o resultado:\n{listaC}')
if __name__ == '__main__':
    main()
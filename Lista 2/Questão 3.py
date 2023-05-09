'''3) Faça um programa que dada uma seqüência de n números, imprimi-la na ordem inversa à da leitura'''
def inverterlista(l):
    l.reverse()
    return l 


def main():
    while True:
        try:
            n = int(input('Quantos números vai ter a sua sequência?\n'))
            listanums = []
            for i in range(n):
                num = float(input(f'Digite o {i+1}º NÚMEROS.\n'))
                listanums.append(num)
                
            listanums = inverterlista(listanums)
                
            print(f'A Sequência criada invertida:\n{listanums}')
            break
        except:
            print('Digite somente NÚMEROS!!!')
if __name__ == '__main__':
    main()
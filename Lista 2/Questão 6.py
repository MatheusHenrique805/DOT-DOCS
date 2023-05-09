'''6) Dadas duas listas, uma contendo a quantidade e a outra o preço de 20 produtos, elabore um programa que calcule e exiba o faturamento que é igual a quantidade x preço. Calcule e exiba também o faturamento total que é o somatório de todos os faturamentos, a média dos faturamentos e quantos faturamentos estão abaixo da média'''
def calc_media(lista, fat_total):
    media = fat_total / len(lista)
    contagem = 0
    for faturamento in lista:
        if faturamento < media:
            contagem += 1
        else:
            pass
    
    return media, contagem


def exibir(lqtd, lpre):
    fatura_total = 0
    lista_fat = []
    saida_fat = f''
    
    for i in range(len(lqtd)):
        faturamento = lqtd[i] * lpre[i]
        saida_fat += f'{i+1}º Faturamento: R${faturamento:.2f}\n'
        lista_fat.append(faturamento)
        fatura_total += faturamento
    
    media_fat, abaixo_media = calc_media(lista_fat, fatura_total)    
       
    saida_fat += f'\nFaturamento total: R${fatura_total:.2f}\nMedia: R${media_fat:.2f}\nQtd de faturamentos abaixo da media {abaixo_media}'

    return saida_fat
        
def criar_listas():
    while True:
        try:
            listaq = []
            listap = []
            for i in range(20):
                qtd = int(input(f'Quantas unidades do {i+1}º produto?\n'))
                if qtd > 0:
                    preco = float(input('Valor do produto?\nR$'))
                    if preco > 0:
                        listaq.append(qtd)
                        listap.append(preco)
                    else:
                        while preco <= 0:
                            preco = float(input('Digite novamente.\nR$'))
                            if preco > 0:
                                listap.append(qtd)
                            else:
                                pass
                else:
                    raise ValueError
            break
        except ValueError:
            print('DADO INCOERENTE!!')
            
    return listaq, listap


def main():
    lista_qtds, lista_preco = criar_listas()
    
    print(exibir(lista_qtds, lista_preco))
    
if __name__ == '__main__':
    main()
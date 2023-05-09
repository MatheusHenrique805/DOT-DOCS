'''17) Ler uma lista W de 10 elementos, depois ler um valor V. Contar e escrever quantas vezes o valor V ocorre na lista W e escrever também em que posições (índices) da lista W o valor V aparece. Caso o valor V não ocorra nenhuma vez na lista W, escrever uma mensagem informando isto'''
def verificar_valor(listaw):
    while True:
        try:
            contador = 0
            posicoes = []
            valor = float(input('Digite o  valor V.\n'))
            
            for i in range(len(listaw)):
                if listaw[i] == valor:
                    contador += 1
                    posicoes.append(i+1)
                else:
                    pass
            break
        except:
            print('INFORMAÇAO INCORRETA!!')
    
    return f'O número de ocorrências do valor V {valor} é {contador}, nas posições: {posicoes}' if contador > 0 else 'Ocorrência nula'       
 
            
def main():
    while True:
        try:
            listaw = []
            for i in range(10):
                elemento = float(input(f'Digite o {i+1}º valor a entrar na lista W.\n'))
                listaw.append(elemento)
                
            verificação = verificar_valor(listaw)
        
            print(verificação)
        except:
            print('SÓ VALORES NÚMERICO POR FAVOR!!')
if __name__ == '__main__':
    main()
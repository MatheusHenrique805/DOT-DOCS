'''7) Dada uma lista contendo 10 elementos numéricos, elabore um programa que verifique se um outro valor dado pertence ou não à lista'''
def verificar_valor(lista, valor):
    
    return valor in lista
   
        
def criar_lista():
    while True:
        try:
            lista =[]
            
            for i in range(10):
                num = float(input(f'Digite o {i+1}º número da lista.\n'))
                lista.append(num)
            break
        except:
            print('DADO NÃO NÚMERICO!!') 
    
    return lista  

   
def main():
    listanums = criar_lista()
    while True:
        try:
            valor = float(input('Digite um número para verificar se ele existe nessa lista.\n'))
            
            if verificar_valor(listanums, valor):
                print(f'{valor} pertence à lista.')
                break
            else:
                print(f'{valor} não pertence à lista.')
                break
        except:
            print('DADO INVÁLIDO!!!')
    
if __name__ == '__main__':
    main()
'''10)Escreva uma função que recebe uma lista com n números inteiros, e determina a masoma_max soma dos números que se repetem da lista. Ex: [5, -2, -2, 5, 3, 5, 10, -2, 3, 10, 3, 1] = 20'''
def det_soma_max(lista):
    if len(lista) <= 1:
        return Exception
    else:
        registro_qtd = {}
        repetidos = []
        for numero in lista:
            if type(numero) != int:
                return Exception
            if numero not in registro_qtd:
                registro_qtd[numero] = 1
            else:
                registro_qtd[numero] += 1
                repetidos += [numero]
                
        soma_max = 0
        soma = 0 
        for numero in repetidos:
            soma = numero * registro_qtd[numero]        
            if repetidos.index(numero) == 0:
                soma_max = soma
            elif soma > soma_max:
                soma_max = soma
            else:
                continue
    
    return soma_max

assert det_soma_max([]) == Exception
assert det_soma_max([299]) == Exception
assert det_soma_max([12, 76, 43, '']) == Exception
assert det_soma_max([1, 99, 32, False]) == Exception
assert det_soma_max([21, 65, 787, 4345, 44, 787, 2.9]) == Exception
assert det_soma_max([-2, -2]) == -4
assert det_soma_max([5, -2, -2, 5, 3, 5, 10, -2, 3, 10, 3, 1]) == 20
assert det_soma_max([1, -1, 1, -1]) == 2 
assert det_soma_max([0, 0, 0, 0]) == 0
assert det_soma_max([0, 1, 0]) == 0
assert det_soma_max([100, 324, 243, 324, 100, 243]) == 648
assert det_soma_max([-1, -3, -3, -1, -2, -1, -2]) == -3
print('Aprovada!!!')

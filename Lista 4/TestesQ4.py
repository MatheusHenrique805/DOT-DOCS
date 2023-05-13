'''4) Escreva uma função que recebe uma lista com n números inteiros, e determina a maior soma de qualquer seguimento da lista. Ex: [5, -2, -2, -7, 3, 15, 10, -3, 9, -6, 4, 1] = 34'''
def somar_seguimentos(lista):
    if len(lista) <= 1:
        return Exception
    else:
        for num in lista:
            if type(num) != int:
                return Exception
            else:
                continue
        
        soma = lista[0]
        soma_maxima = lista[0]
        for i in range(1, len(lista)):
            if soma + lista[i] > lista[i]:
                soma = soma + lista[i]
                if soma > soma_maxima:
                    soma_maxima = soma
                else:
                    continue
            elif soma + lista[i] < lista[i]:
                soma = lista[i]
                if soma > soma_maxima:
                    soma_maxima = soma
                else:
                    continue
            else:
                continue
    
    return soma_maxima            


assert somar_seguimentos([]) == Exception
assert somar_seguimentos([1, 'rd', 212]) == Exception
assert somar_seguimentos([1133]) == Exception
assert somar_seguimentos([False, 21, 54]) == Exception
assert somar_seguimentos([12.45, 32]) == Exception
assert somar_seguimentos([23, 34]) == 57
assert somar_seguimentos([0, 0, 0, 0]) == 0
assert somar_seguimentos([1, 1, 1, 1, 1, 1]) == 6
assert somar_seguimentos([2, 1, 4]) == 7
assert somar_seguimentos([2, 5, -3, 21, -12, -3]) == 25
assert somar_seguimentos([-27, -55, -8, -92, -14]) == -8
print('Aprovada!!!')
'''6) Escreva uma função que recebe uma lista com n números inteiros, e retorna True caso a lista esteja ordenada em ordem ascendente ou False caso não esteja ordenada. Ex [1, 2, 3] = True. Ex. [3, 7, 2] = False'''
def verificar_ascendencia(lista):
    if len(lista) == 0:
        return Exception
    else:
        contagem = 0
        for index in range(len(lista)):
            if type(lista[index]) != int:
                return Exception
            if 0 == index or lista[index] > lista[index - 1]:
                continue
            elif lista[index] < lista[index - 1]:
                return False
            else:
                contagem += 1
    
    return True if contagem < len(lista) - 1 else Exception


assert verificar_ascendencia([]) == Exception
assert verificar_ascendencia([True, 12, 32]) == Exception
assert verificar_ascendencia([2.5, 1, 25]) == Exception
assert verificar_ascendencia(['a', 12]) == Exception
assert verificar_ascendencia([1, 1, 1, 1]) == Exception
assert verificar_ascendencia([1, 2, 3]) == True
assert verificar_ascendencia([23, 34, 43]) == True
assert verificar_ascendencia([1, -1, 20]) == False
assert verificar_ascendencia([12, 11, 100]) == False
assert verificar_ascendencia([-1, -2, -3, -4]) == False
assert verificar_ascendencia([-8, -7, -6, -4, -3, -2]) == True
assert verificar_ascendencia([1, 2, 2, 3, 3, 3, 3]) == True
assert verificar_ascendencia([1, 45, 65, 65, 65, 65, 65, 65, 2]) == False
print('Aprovada!!!')
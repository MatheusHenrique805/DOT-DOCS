'''9) Escreva uma função que recebe uma lista com n números inteiros, retornar uma lista eliminando todas as ocorrências de valores repetidos. Ex: [5, 4, 5, 7, 3, 4] = [7, 3]'''
def eliminar_repetidos(lista):
    if len(lista) == 0:
        return Exception
    else:
        registro_qtd = {}
        for num in lista:
            if type(num) != int:
                return Exception
            if num not in registro_qtd:
                registro_qtd[num] = 1
            else:
                registro_qtd[num] += 1
                
        sem_repetidos = []
        for num in lista:
            if registro_qtd[num] == 1:
                sem_repetidos.append(num)
            else:
                continue
    
    return sem_repetidos


assert eliminar_repetidos([]) == Exception
assert eliminar_repetidos([2, 1, 43, '']) == Exception
assert eliminar_repetidos([43, 65, True]) == Exception
assert eliminar_repetidos([322, 212, 212.322]) == Exception
assert eliminar_repetidos([22, 22]) == ([])
assert eliminar_repetidos([2]) == ([2])
assert eliminar_repetidos([5, 4, 5, 7, 3, 4]) == ([7, 3])
assert eliminar_repetidos([54, -1, -1, 32, 54]) == ([32])
assert eliminar_repetidos([65, 9, 0, 9, 65, 1, 4]) == ([0, 1, 4])
print('Aprovada!!!!')
'''5) Escreva uma função que recebe uma lista com n números inteiros, e retorna uma lista com a soma cumulativa dos elementos da lista original onde o i-ésimo elemento é a soma dos primeiros i+1 elementos da lista original. Ex: [1,2,3] = [1,3,6]'''
def somar_valores(lista):
    if len(lista) == 0:
        return Exception
    else:
        lista_somas =[] 
        soma = 0
        for num in lista:
            if type(num) != int:
                return Exception
            else:
                soma += num
                lista_somas.append(soma)
    
    return lista_somas            


assert somar_valores([]) == Exception
assert somar_valores([21, '12']) == Exception
assert somar_valores([4.1, 2.5]) == Exception
assert somar_valores([21, True, 23, 43]) == Exception
assert somar_valores([2]) == ([2])
assert somar_valores([2, 23]) ==  ([2, 25])
assert somar_valores([1, -1, 1, -1, 2]) == ([1, 0, 1, 0, 2])
assert somar_valores([1, 2, 3]) == ([1, 3, 6])
assert somar_valores([1, 1, 1, 1]) == ([1, 2, 3, 4])
assert somar_valores([-2, -12, -3, -32]) == ([-2, -14, -17, -49])
assert somar_valores([1, -32, -12, 12]) == ([1, -31, -43, -31])
assert somar_valores([0, 0, 0, 0, 0]) == ([0, 0, 0, 0, 0])
assert somar_valores([0, 200, 2, 87]) == ([0, 200, 202, 289])
print('Aprovada!!!')
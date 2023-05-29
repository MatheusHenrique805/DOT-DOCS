'''7. Escreva uma função chamada "encontrar_elemento_faltantse" que receba uma lista de números de 1 a n (sendo n um número inteiro) em ordem aleatória, com um elemento faltando, e retorne o elemento que está faltando. Ex: [4,3,1,5] = 2'''
def encontra_e_faltante(lista):
    if len(lista) <= 1:
        return Exception
    if 0 in lista:
        return Exception
    
    for num in lista:
        if type(num) != int:
            return Exception 
    else:
        max_num = 0
        for num in lista:
            if max_num == 0:
                max_num = num
            elif num > max_num:
                max_num = num
            else:
                continue
            
        lista_pura = []
        faltante = 0
        for i in range(1, max_num + 1):
            lista_pura.append(i)
            if i not in lista:
                faltante = i
            else:
                continue
            
    return faltante if len(lista_pura) - len(lista) == 1 else Exception


assert encontra_e_faltante([]) == Exception
assert encontra_e_faltante(['2313', 3547]) == Exception
assert encontra_e_faltante([12.4, 457, 143]) == Exception
assert encontra_e_faltante([True, 4, 7, 5]) == Exception
assert encontra_e_faltante([1, 3, 5]) == Exception
assert encontra_e_faltante([1, 2, 3]) == Exception
assert encontra_e_faltante([0, 2]) == Exception
assert encontra_e_faltante([5, 4, 9, 6, 7, -1, 3, 2, 8]) == Exception
assert encontra_e_faltante([4, 6, 8, 2]) == Exception
assert encontra_e_faltante([4, 8, 3, 7, 2, 1, 5, 6]) == Exception
assert encontra_e_faltante([4, 3, 1, 5]) == 2
assert encontra_e_faltante([3, 1, 5, 2]) == 4
assert encontra_e_faltante([2, 7, 1, 3, 8, 5, 4]) == 6
assert encontra_e_faltante([12, 7, 14, 11, 3, 10, 8, 4, 2, 6, 1, 13, 15, 9]) == 5
print('Testes OK!!!')

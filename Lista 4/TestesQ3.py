'''3) Escreva uma função que recebe uma lista com n números inteiros, e determina a maior soma de um segmento com 2 valores. Ex: [5, -2, -2, -7, 3, 15, 10, -3, 9, -6,
4, 1] = 25'''
def det_maior_soma(lista):
    soma = 0
    maior_sum = 0
    if len(lista) == 0:
        return Exception
    else:
        for num in lista:
            if type(lista[i]) != int:
                return Exception
        for i in range(len(lista) - 1):
            soma = lista[i] + lista[i+1]
            if i == 0:
                maior_sum = soma
            elif soma > maior_sum:
                maior_sum = soma
            else:
                continue

    return maior_sum


assert det_maior_soma([]) == Exception
assert det_maior_soma(['', '']) == Exception
assert det_maior_soma([True]) == Exception
assert det_maior_soma([4.5]) == Exception
assert det_maior_soma([5, -2, -2, -7]) == 3
assert det_maior_soma([10, -405, 1562, 50, -1153, 56]) == 1612
assert det_maior_soma([-12, -211, -14, -234, -321]) == -223
print('Aprovada!!!')

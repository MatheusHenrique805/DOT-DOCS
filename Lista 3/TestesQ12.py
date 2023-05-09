'''12. Faça uma função que recebe 2 valores inteiros por parâmetro e retorna-os ordenados em ordem crescente'''
def ordenar_crescente(x, y):
    if type(x) != int or type(y) != int:
        return Exception
    if x >= y:
        maior = x
        menor = y
    elif x < y:
        maior = y
        menor = x
    else:
        pass
    
    return menor, maior


assert ordenar_crescente('Dois', 6) == Exception
assert ordenar_crescente(2, 'Seis') == Exception
assert ordenar_crescente(12, 1.2) == Exception
assert ordenar_crescente(True, 1) == Exception
assert ordenar_crescente(1, False) == Exception
assert ordenar_crescente(23, 12) == (12, 23)
assert ordenar_crescente(-1, 0) == (-1, 0)
assert ordenar_crescente(0, 0) == (0, 0)
assert ordenar_crescente(1, 1) == (1, 1)
assert ordenar_crescente(0, 1) == (0, 1)
assert ordenar_crescente(-12, -12) == (-12, -12)
print('Aprovada!!!')
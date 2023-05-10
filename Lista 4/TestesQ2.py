'''2) Escreva uma função que recebe uma lista com n números inteiros, conta e imprime o número de vezes que cada número ocorre na sequência.'''
def registrar_quantidade(lista):
    if len(lista) == 0:
        return Exception
    registro_qtd = {}
    for numero in lista:
        if type(numero) != int:
            return Exception
        if numero not in registro_qtd:
            registro_qtd[numero] = 1
        else:
            registro_qtd[numero] += 1
    
    return registro_qtd

assert registrar_quantidade([]) == Exception
assert registrar_quantidade(["", 2, ""]) == Exception
assert registrar_quantidade([10, 10.3]) == Exception
assert registrar_quantidade([False, 4, False]) == Exception
assert registrar_quantidade([5, 5, 6, 4, 7, 3, 6, 8, 4, 6, 4, 6, 1, 5, 4, 4]) == ({1: 1, 3: 1, 4: 5, 5: 3, 6: 4, 7: 1, 8: 1})
assert registrar_quantidade([0, 0, 0, 0, 0, 1, 1,]) == ({0: 5, 1: 2})
assert registrar_quantidade([1, 2, 3, 4]) == ({1: 1, 2: 1, 3: 1, 4: 1})
assert registrar_quantidade([-1, -2, -2, 3]) == ({-1: 1, -2: 2, 3: 1})
print('Aprovada!!!') 
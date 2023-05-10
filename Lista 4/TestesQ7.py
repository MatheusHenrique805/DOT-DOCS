'''7) Escreva uma função que recebe uma lista com n números inteiros, e retorna True caso algum elemento apareça mais de uma vez ou False caso nenhum elemento apareça mais de uma vez. Ex [1, 2, 3, 1] = True. Ex. [3, 7, 2, 4] = False.'''
def verificar_repeticao(lista):
    if len(lista) == 0:
        return Exception
    else:
        lista2 = []
        for num in lista:
            if type(num) != int:
                return Exception
            if num not in lista2:
                lista2.append(num)
            else:
                return True
    
    return False
                
        
assert verificar_repeticao([]) == Exception
assert verificar_repeticao(['', 21, 0]) == Exception
assert verificar_repeticao([12, 32, True]) == Exception
assert verificar_repeticao([1.0, 1.0]) == Exception
assert verificar_repeticao([1, 2, 3, 1]) == True
assert verificar_repeticao([3, 7, 2, 4]) == False
assert verificar_repeticao([0, 0, 0, 1, 3, 5, 6]) == True
assert verificar_repeticao([1, -1, 2, -2, -3, 3]) == False
assert verificar_repeticao([23, 34, 43]) == False
assert verificar_repeticao([1, 1, 1, 1]) == True
assert verificar_repeticao([123, 111, 21, 324, 1111, 1234]) == False
assert verificar_repeticao([1, -1, 1, -1]) == True
print('Aprovada!!!')
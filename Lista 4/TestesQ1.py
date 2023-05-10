'''1) Escreva uma função que recebe uma lista com n números inteiros, retornar uma lista eliminando as repetições. Ex: [5, 4, 5, 7, 3, 4] = [5, 4, 7, 3]'''
def eliminar_repeticoes(lista):
    if len(lista) == 0:
        return Exception
    else:
        sem_repet = []
        for num in lista:
            if type(num) != int:
                return Exception
            if num not in sem_repet:
                sem_repet.append(num)
            else:
                continue

    return sem_repet
    


assert eliminar_repeticoes([]) == Exception
assert eliminar_repeticoes(["", 0]) == Exception
assert eliminar_repeticoes([True, 4, True]) == Exception
assert eliminar_repeticoes([5.4, 34, 12]) == Exception
assert eliminar_repeticoes([54, 32, 12, 45, 1]) == ([54, 32, 12, 45, 1])
assert eliminar_repeticoes([5, 4, 5, 7, 3, 4]) == ([5, 4, 7, 3])
assert eliminar_repeticoes([-1, -2, -2, -3]) == ([-1, -2, -3])
print('Aprovada!!!')

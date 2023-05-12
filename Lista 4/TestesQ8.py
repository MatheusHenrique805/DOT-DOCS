'''8) Escreva uma função que recebe uma lista com n números inteiros, e retorna o valor mais próximo da média de valores da lista. Ex [2.5, 7.5, 10.0, 4.0] = 7.5'''
def definir_maisprox(lista):
    if len(lista) <= 1:
        return Exception
    else:
        soma = 0
        media = 0
        for num in lista:
            if type(num) != int:
                return Exception
            soma += num
        media = soma / len(lista)
        
        dif = 0
        menor_dif = 0
        num_prox = 0
        for num in lista:
            dif = -(num - media)
            if dif < 0:
                dif = -(dif)
            if menor_dif == 0 or dif < menor_dif:
                num_prox = num
                menor_dif = dif
            else:
                continue
        
    return num_prox 
            
        
assert definir_maisprox([]) == Exception
assert definir_maisprox(['a', 21, 3]) == Exception
assert definir_maisprox([True, 1]) == Exception
assert definir_maisprox([2, 2.5]) == Exception
assert definir_maisprox([0]) == Exception
assert definir_maisprox([2, 3]) == 2
assert definir_maisprox([2, 7, 10, 4]) == 7 # Eu estou seguindo o que está escrito no enunciado e não o exemplo
assert definir_maisprox([3, 2, 5, 7, 4]) == 4
assert definir_maisprox([10, 10 , 10]) == 10
assert definir_maisprox([2, 15, 76, 45]) == 45
assert definir_maisprox([-1, -4, 6, -3]) == -1
assert definir_maisprox([-1, -3, -10, -13, -4]) == -4
print('Aprovada!!!')
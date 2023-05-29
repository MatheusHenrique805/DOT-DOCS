'''9. Escreva uma função chamada "encontrar_elemento_repetido" que receba uma lista de números como parâmetro e retorne o elemento que se repete mais vezes na lista.'''
def encontrar_e_repetido(lista):
    if len(lista) <= 1:
        return Exception
    for num in lista:
        if type(num) != int and type(num) != float:
            return Exception
    else:
        registro_repet= {}
        for num in lista:
            if num not in registro_repet:
                registro_repet[num] = 1
            else:
                registro_repet[num] += 1
    
        num_mais_repetido = 0
        contagem_repet = 0
        contagem = 0
        for key in registro_repet:
            if registro_repet[key] > contagem_repet and registro_repet[key] != 1:
                num_de_ocorrencias = registro_repet[key]
                num_mais_repetido = key
            if registro_repet[key] != 1:
                contagem += 1
            else:
                continue
            
    return num_mais_repetido if num_de_ocorrencias > contagem else Exception

 
assert encontrar_e_repetido([]) == Exception
assert encontrar_e_repetido([12, 45.6, 32. -12, '43']) == Exception
assert encontrar_e_repetido([32, 45.6, True]) == Exception
assert encontrar_e_repetido([12.21]) == Exception
assert encontrar_e_repetido([3.5, 2]) == Exception
assert encontrar_e_repetido([13.34, 13.34]) == 13.34
assert encontrar_e_repetido([1, 2, 3, -4, 4, 5, 6, 6.0, 7, 8, 9, 9]) == Exception
assert encontrar_e_repetido([3, 2, 8.43, 7, -5, 9, 3, 1, 5, 6, 12]) == 3
assert encontrar_e_repetido([-1, -65.34, -34, -34, 0, 0, 0]) == 0
assert encontrar_e_repetido([-1, -65.34, -34, -34,]) == -34
print('Testes OK!!!')
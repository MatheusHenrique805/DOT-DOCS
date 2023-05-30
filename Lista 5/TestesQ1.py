'''1. Crie uma função chamada "encontrar_primos_gemeos" que receba um número inteiro n como parâmetro e retorne uma lista contendo todos os pares de números primos
gêmeos menores que n. Os números primos gêmeos são dois números primos consecutivos que diferem em 2.'''
def retornar_primos(num):
    divisores = []
    for i in range(1, num + 1):
        if 2 % i == 0:
            divisores.append(i)
        else:
            continue
    
    return True if len(divisores) == 2 else False


def encontrar_primos_gemeos(numero):
    if type(numero) != int or numero <= 3:
        return Exception
    else:
        lista_primos = []
        for i in range(1, numero + 1):
            if retornar_primos(i) == True:
                lista_primos.append(i)
            else:
                continue

        lista_gemeos = []
        for indice in range(len(lista_primos) - 1):
            if lista_primos[indice + 1] - lista_primos[indice] == 2:
                lists_gemeos.append(lista_primos[indice], lista_primos[indice + 1])
            else:
                continue
    
    return lista_gemeos

    
assert encontrar_primos_gemeos(0) == Exception
assert encontrar_primos_gemeos(12.4) == Exception
assert encontrar_primos_gemeos(True) == Exception
assert encontrar_primos_gemeos('12') == Exception
assert encontrar_primos_gemeos(1) == Exception
assert encontrar_primos_gemeos(2) == Exception
assert encontrar_primos_gemeos(-21) == Exception
assert encontrar_primos_gemeos(3) == Exception
assert encontrar_primos_gemeos(4) == ([])
assert encontrar_primos_gemeos(5) == ([])
assert encontrar_primos_gemeos(9) == ([5, 7])
assert encontrar_primos_gemeos(6) == ([3, 5])
assert encontrar_primos_gemeos(17) == ([3, 5, 5, 7, 11, 13])
assert encontrar_primos_gemeos(18) == ([3, 5, 5, 7, 11, 13])
assert encontrar_primos_gemeos(21) == ([3, 5, 5, 7, 11, 13, 17, 19])
print('Testes OK!!!')

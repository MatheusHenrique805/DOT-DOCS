'''24. Escreva uma função que recebe, por parâmetro, dois valores X e Z e calcula e retorna X^Z. (sem utilizar funções ou operadores de potência prontos).'''
def calcular(x, z):
    if (type(x) != int and type(x) != float) or (type(z) != int):
        return Exception
    if z < 0:
        denominador = x
        for _ in range(1, -(z)):
            denominador *= x
        resultado = 1 / denominador
    else:
        resultado = x
        for _ in range(1, z):
            resultado *= x
    
    return round(resultado, 2) if z != 0 else 1
        
assert calcular('x', 3) == Exception
assert calcular(2, 'z') == Exception
assert calcular(True, 2) == Exception
assert calcular(4, False) == Exception
assert calcular(12, 2.1) == Exception
assert calcular(-3 , 3) == -27
assert calcular(3, -3) == 0.04
assert calcular(0, 12) == 0
assert calcular(12, 0) == 1
assert calcular(0, 0) == 1
assert calcular(2, 3) == 8
assert calcular(2.4, 2) == 5.76
assert calcular(10, 4) == 10000
print('Aprovada!!!')
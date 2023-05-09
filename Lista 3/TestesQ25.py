'''25. Escreva uma função que recebe, por parâmetro um valor inteiro e retorna o seu fatorial.'''
def calcular_fatorial(valor):
    if type(valor) != int or valor < 0:
        return Exception
    else:
        fatorial = 1
        for n in range(1, valor + 1):
            fatorial *= n
    
    return fatorial if valor != 0 else 1
assert calcular_fatorial('q') == Exception
assert calcular_fatorial(-21) == Exception
assert calcular_fatorial(4.4) == Exception
assert calcular_fatorial(True) == Exception
assert calcular_fatorial(0) == 1
assert calcular_fatorial(3) == 6
assert calcular_fatorial(4) == 24
assert calcular_fatorial(2) == 2
assert calcular_fatorial(1) == 1
assert calcular_fatorial(5) == 120
print('Aprovada!!!')
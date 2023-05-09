'''21. Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S.
                                S = 1 + ½ + 1/3 + ¼ + 1/5 + 1/N.'''
def calcular_s(n):
    if type(n) != int or n <= 0:
        return Exception
    else:
        s = 0
        for num in range(1, n + 1):
            s += 1 / num
    
    return round(s, 1)


assert calcular_s('') == Exception
assert calcular_s(True) == Exception
assert calcular_s(1.5) == Exception
assert calcular_s(0) == Exception
assert calcular_s(-1) == Exception
assert calcular_s(3) == 1.8
assert calcular_s(1) == 1
assert calcular_s(5) == 2.3
assert calcular_s(2) == 1.5
assert calcular_s(9) == 2.8
print('Aprovada!!!')
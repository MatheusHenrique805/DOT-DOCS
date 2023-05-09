'''22. Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S.
                                S = 1 + 1/1! + ½! + 1/3! + 1 /N!'''
def calcular_s(n):
    if type(n) != int or n <= 0:
        return Exception
    else:
        denominador = 1
        s = 1
        for i in range(1, n + 1):
            denominador *= i
            s += 1 / denominador  
    
    return round(s, 1)


assert calcular_s('trelo') == Exception
assert calcular_s(False) == Exception
assert calcular_s(5.8) == Exception
assert calcular_s(0) == Exception
assert calcular_s(-243) == Exception
assert calcular_s(3) == 2.7
assert calcular_s(1) == 2
assert calcular_s(5) == 2.7
assert calcular_s(2) == 2.5
assert calcular_s(9) == 2.7
print('Aprovada!!!')
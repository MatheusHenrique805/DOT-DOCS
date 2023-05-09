'''23. Escreva uma função que recebe por parâmetro um valor inteiro e positivo N e retorna o valor de S.
                        S = 2/4 + 5/5 + 10/6 + 17/7 + 26/8 + ... +(n2+1)/(n+3)'''
def calcular_s(n):
    if type(n) != int or n <= 0:
        return Exception
    else:
        s = 0
        for i in range(1, n + 1):
            s  += (i ** 2 + 1) / (i + 3)
    
    return round(s, 1)


assert calcular_s('trelo') == Exception
assert calcular_s(False) == Exception
assert calcular_s(5.8) == Exception
assert calcular_s(0) == Exception
assert calcular_s(-53) == Exception
assert calcular_s(3) == 3.2
assert calcular_s(1) == 0.5
assert calcular_s(5) == 8.8
assert calcular_s(2) == 1.5
assert calcular_s(9) == 30.7
print('Aprovada!!!')
'''10. Escreva uma função chamada "verificar_quadrado_perfeito" que receba um número inteiro como parâmetro e retorne True se o número for um quadrado perfeito, e False caso contrário. Um número inteiro é considerado um quadrado perfeito quando ele é o resultado da multiplicação de um número inteiro por ele mesmo. Em outras palavras, um número inteiro "n" é um quadrado perfeito se existir um número inteiro "m" tal que "n =
m * m". Por exemplo, os números 4, 9, 16 e 25 são quadrados perfeitos, pois podem ser
obtidos pela multiplicação de um número inteiro por ele mesmo: 4 = 2 * 2; 9 = 3 * 3; 16 =
4 * 4; 25 = 5 * 5.
Obs: não uilizar a função raiz quadrada isqrt()'''
def verificar_quadrado_perfeito(n):
    if type(n) != int or n <= -1:
        return Exception
    else:
        m = int(n ** (1/2))
        if n == m * m:
            return True
        else:
            return False
        

assert verificar_quadrado_perfeito([]) == Exception
assert verificar_quadrado_perfeito(()) == Exception
assert verificar_quadrado_perfeito({}) == Exception
assert verificar_quadrado_perfeito('4') == Exception
assert verificar_quadrado_perfeito(4.9) == Exception
assert verificar_quadrado_perfeito(True) == Exception
assert verificar_quadrado_perfeito(-16) == Exception
assert verificar_quadrado_perfeito(-1) == Exception
assert verificar_quadrado_perfeito(0) == True
assert verificar_quadrado_perfeito(4) == True
assert verificar_quadrado_perfeito(9) == True
assert verificar_quadrado_perfeito(36) == True
assert verificar_quadrado_perfeito(81) == True
assert verificar_quadrado_perfeito(16) == True
assert verificar_quadrado_perfeito(25) == True
assert verificar_quadrado_perfeito(100) == True
assert verificar_quadrado_perfeito(32) == False
assert verificar_quadrado_perfeito(2) == False
assert verificar_quadrado_perfeito(10) == False
assert verificar_quadrado_perfeito(12) == False
assert verificar_quadrado_perfeito(6) == False
assert verificar_quadrado_perfeito(56) == False
assert verificar_quadrado_perfeito(20) == False
print('Testes OK!!!')
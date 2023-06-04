'''4. Crie uma função chamada "contar_divisores" que receba um número inteiro como parâmetro e retorne a quantidade de divisores desse número.'''
def contar_divisores(num):
    if type(num) != int or num == 0:
        return Exception
    else:
        contagem = 0
        if num <= -1:
            for i in range(1, -num + 1):
                if num % i == 0:
                    contagem += 1
                else:
                    continue
        else:
            for i in range(1, num + 1):
                if num % i == 0:
                    contagem += 1
                else:
                    continue
    
    return contagem 



assert contar_divisores([]) == Exception
assert contar_divisores(()) == Exception
assert contar_divisores({}) == Exception
assert contar_divisores('12') == Exception
assert contar_divisores(12.1) == Exception
assert contar_divisores(False) == Exception
assert contar_divisores(0) == Exception
assert contar_divisores(1) == 1
assert contar_divisores(-1) == 1
assert contar_divisores(3) == 2
assert contar_divisores(10) == 4
assert contar_divisores(-10) == 4
assert contar_divisores(23) == 2
assert contar_divisores(9) == 3
assert contar_divisores(2) == 2
assert contar_divisores(5) == 2
assert contar_divisores(20) == 6
assert contar_divisores(100) == 9
print('Testes OK!!!') 



'''19. Faça uma função que recebe, por parâmetro, um valor inteiro e positivo e retorna o número de divisores desse valor'''
def contar_divisores(valor):
    if type(valor) != int or valor <= 0:
        return Exception
    else:
        quant_divisores = 0
        for n in range(1, valor + 1):
            if valor % n == 0:
                quant_divisores += 1
            else:continue
    
    return quant_divisores


assert contar_divisores('numero') == Exception
assert contar_divisores(-21) == Exception
assert contar_divisores(0) == Exception
assert contar_divisores(2.56) == Exception
assert contar_divisores(False) == Exception
assert contar_divisores(1) == 1
assert contar_divisores(3) == 2
assert contar_divisores(2) == 2
assert contar_divisores(4) == 3
assert contar_divisores(10) == 4
assert contar_divisores(6) ==  4
assert contar_divisores(20) == 6
print('Aprovada!!!')
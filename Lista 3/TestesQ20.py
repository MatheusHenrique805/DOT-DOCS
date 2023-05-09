'''20. Escreva uma função que recebe, por parâmetro, um valor inteiro e positivo e retorna o somatório desse valor'''
def calcular_somatorio(valor):
    if type(valor) != int or valor <= 0:
        return Exception
    else:
        soma = 0
        for num in range(1, valor + 1):
            soma += num
    
    return soma


assert calcular_somatorio('.;=') == Exception
assert calcular_somatorio(0) == Exception
assert calcular_somatorio(-1) == Exception
assert calcular_somatorio(12.3) == Exception
assert calcular_somatorio(True) == Exception
assert calcular_somatorio(2) == 3
assert calcular_somatorio(1) == 1
assert calcular_somatorio(4) == 10
assert calcular_somatorio(10) == 55
print('Aprovada!!!')
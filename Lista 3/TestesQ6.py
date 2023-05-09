'''6. Faça uma função que verifique se um valor é perfeito ou não. Um valor é dito perfeito quando ele é igual à soma dos seus divisores excetuando ele próprio. (Ex: 6 é perfeito, 6 = 1 + 2 + 3, que são seus divisores). A função deve retornar
um valor booleano'''
def verificar_perfeito(n):
    if type(n) != int or n <= 1:
        return Exception
    else:
        soma = 0
        for valor in range(1, n):
            if n % valor == 0:
                soma += valor
            else: continue

    return 'É perfeito' if soma == n else 'Não é perfeito'


assert verificar_perfeito('seis') == Exception
assert verificar_perfeito(0) == Exception
assert verificar_perfeito(-1) == Exception
assert verificar_perfeito(3.0) == Exception
assert verificar_perfeito(1) == Exception
assert verificar_perfeito(False) == Exception
assert verificar_perfeito(6) == 'É perfeito'
assert verificar_perfeito(11) == 'Não é perfeito'
assert verificar_perfeito(2) == 'Não é perfeito'
assert verificar_perfeito(28) == 'É perfeito'
print('Aprovada!!!')
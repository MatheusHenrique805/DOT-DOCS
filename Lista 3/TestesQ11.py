'''11. Faça uma função que recebe, por parâmetro, a altura e o sexo de uma pessoa e retorna o seu peso ideal. Para homens, calcular o peso ideal usando a fórmula peso ideal = 72.7 * altura - 58 e, para mulheres, peso ideal = 62.1 * altura - 44.7.'''
def calcular_pesoideal(altura, sexo):
    if (type(altura) != float or type(sexo) != str) or (sexo != 'F' and sexo != 'M'):
        return Exception
    if altura < 1.00 or altura > 2.20:
        return Exception
    if sexo == 'F':
        peso_i = round(62.1 * altura - 44.7, 1)
    else:
        peso_i = round(72.7 * altura - 58, 1)
    
    return peso_i
    

assert calcular_pesoideal('abc', 'F') == Exception
assert calcular_pesoideal(0.00, 'M') == Exception
assert calcular_pesoideal(-1.74, 'F') == Exception
assert calcular_pesoideal(1.78, 'S') == Exception
assert calcular_pesoideal('M', 1.65) == Exception
assert calcular_pesoideal(1.54, '@') == Exception
assert calcular_pesoideal(True, 'M') == Exception
assert calcular_pesoideal('M', False) == Exception
assert calcular_pesoideal(0.99, 'F' ) == Exception
assert calcular_pesoideal(2.21, 'F') == Exception
assert calcular_pesoideal(0.99, 'M') == Exception
assert calcular_pesoideal(2.21, 'M') == Exception
assert calcular_pesoideal(1.00, 'f') == Exception
assert calcular_pesoideal(1.00, 'm') == Exception
assert calcular_pesoideal(1.00, 'F') == 17.4
assert calcular_pesoideal(2.20, 'F') == 91.9
assert calcular_pesoideal(1.01, 'F') == 18.0
assert calcular_pesoideal(2.19, 'F') == 91.3
assert calcular_pesoideal(1.00, 'M') == 14.7
assert calcular_pesoideal(2.20, 'M') == 101.9
assert calcular_pesoideal(1.01, 'M') == 15.4
assert calcular_pesoideal(2.19, 'M') == 101.2
print('Aprovada!!!')
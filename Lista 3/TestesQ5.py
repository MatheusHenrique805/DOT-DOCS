'''5. Faça uma função que recebe a idade de uma pessoa em anos, meses e dias e retorna essa idade expressa em dias'''
def calcular_dias(anos, meses, dias):
    if type(anos) != int or type(meses) != int or type(dias) != int:
        return Exception
    if (anos < 0 or meses < 0 or dias < 0) or (anos == meses == dias == 0):
        return Exception
    if meses > 11 or dias > 29:
        return Exception
    else:
        total_dias = anos * 365 + meses * 30 + dias
    
    return total_dias

 
assert calcular_dias('Dois anos', 'Onze meses', 'Vinte dias') == Exception
assert calcular_dias(18.7, 2, 3) == Exception
assert calcular_dias(14, 11.0, 12) == Exception
assert calcular_dias(14, 11, 12.0) == Exception
assert calcular_dias(12, 5, True) == Exception
assert calcular_dias(False, 5, 3) == Exception
assert calcular_dias (12, 1, True) == Exception
assert calcular_dias(43, 32, 3) == Exception
assert calcular_dias(12, 12, 1) == Exception
assert calcular_dias(12, 10, 30) == Exception
assert calcular_dias(3, 7, 32) == Exception
assert calcular_dias(0, 0, 0) == Exception
assert calcular_dias(-12, 5, 10) == Exception
assert calcular_dias(12, -11, 4) == Exception
assert calcular_dias(12, 11, -29) == Exception
assert calcular_dias(1, 2, 14) == 439
assert calcular_dias(0, 0, 1) == 1
assert calcular_dias(0, 11, 0) == 330
assert calcular_dias(1, 0, 0) == 365
print('Aprovada!!!')
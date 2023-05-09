'''1. Faça uma função que recebe por parâmetro o raio de uma esfera e calcula o seu volume (v = 4/3 * PI * R**3).'''
def calcular_volume(r):
    if type(r) != float and type(r) != int:
        return Exception
    if r <= 0:
        return Exception
    else:
        volume =  round(4 / 3 * 3.14 * r ** 3, 2)
    
    return volume


assert calcular_volume('3') == Exception
assert calcular_volume(0) == Exception
assert calcular_volume(-12) == Exception
assert calcular_volume(True) == Exception
assert calcular_volume(3) == 113.04
assert calcular_volume(3.2) == 137.19
assert calcular_volume(1) == 4.19
assert calcular_volume(2) == 33.49
print('Aprovada!!!')
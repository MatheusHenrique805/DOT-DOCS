'''4. Faça uma função que recebe por parâmetro o tempo de duração de um processo em uma fábrica expressa em segundos e retorna também por parâmetro esse tempo em horas, minutos e segundos'''
def calcular_duração(seg):
    if type(seg) != int or seg <= 0:
        return Exception
    else:
        h = seg // 3600
        min = (seg % 3600) // 60
        s = (seg % 3600) % 60
    
    return h, min, s


assert calcular_duração('seg') == Exception
assert calcular_duração(0) == Exception
assert calcular_duração(3600.0) == Exception
assert calcular_duração(True) == Exception
assert calcular_duração(-3600) == Exception
assert calcular_duração(3600) == (1,0,0)
assert calcular_duração(10800) == (3,0,0)
assert calcular_duração(3661) == (1,1,1)
assert calcular_duração(1) == (0,0,1)
print('Aprovada!!!')
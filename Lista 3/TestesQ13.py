'''13. Faça uma função que recebe, por parâmetro, a hora de inicio e a hora de término de um jogo, ambas subdivididas em 2 valores distintos: horas e minutos. O procedimento deve retornar, também por parâmetro, a duração do jogo em horas e minutos, considerando que o tempo máximo de duração de um jogo é de 24 horas e que o jogo pode começar em um dia e terminar no outro.'''
def calcular_duração(h0, m0, hf, mf):
    if type(h0) != int or type(m0) != int or type(hf) != int or type(mf) != int:
        return Exception
    if h0 < 0 or hf < 0 or m0 < 0 or mf < 0:
        return Exception
    if h0 >= 24 or hf >= 24 or m0 >= 60 or mf >= 60:
        return Exception
    if h0 == hf and m0 < mf:
        return Exception
    if (h0 > hf and m0 < mf) or (h0 > hf and m0 == mf):
        hdur = h0 - hf
        mdur = mf - m0
    elif (h0 < hf and m0 > mf) or (h0 < hf and m0 == mf):
        hdur = hf - h0
        mdur = m0 - mf
    elif h0 > hf and  m0 > mf:
        hdur = h0 - hf
        mdur = m0 - mf
    else:
        hdur = hf - h0
        mdur = mf - m0
    
    return hdur, mdur

 
assert calcular_duração('21h', 22, 20, 54) == Exception
assert calcular_duração(21, '22min', 20, 54) == Exception
assert calcular_duração(21, 22, '22h', 54) == Exception
assert calcular_duração(21, 22, 20, '54min') == Exception
assert calcular_duração(21, 22, 20, False) == Exception
assert calcular_duração(21, 22, 20.0, 54) == Exception
assert calcular_duração(21, -22, 20, 54) == Exception
assert calcular_duração(21, 22, 25, 54) == Exception
assert calcular_duração(32, 32, 21, 30) == Exception
assert calcular_duração(6, 21, 18, 62) == Exception
assert calcular_duração(24, 0, 1, 56) == Exception
assert calcular_duração(21, 60, 1, 51) == Exception
assert calcular_duração(0, 61, 0, 0) == Exception
assert calcular_duração(22, 0, 22, 3) == Exception
assert calcular_duração(21, 54, 10, 22) == (11, 32)
assert calcular_duração(21, 22, 20, 21) == (1, 1)
assert calcular_duração(21, 22, 22, 54) == (1, 32)
assert calcular_duração(15, 0, 3, 0) == (12, 0)
assert calcular_duração(0, 0, 0, 0) == (0, 0) # 24 horas
assert calcular_duração(21, 0, 21, 0) == (0, 0) # 24 horas
print('Função testada com sucesso!!!')
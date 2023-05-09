'''2. Escreva uma função que recebe as 3 notas de um aluno por parâmetro e uma letra. Se a letra for A o procedimento calcula a média aritmética das notas do aluno, se for P, a sua média ponderada (pesos: 5, 3 e 2). A função deve retornar
a média calculada.'''
def calcular_media(n1, n2, n3, tipo):
    if (type(n1) == str or type(n1) == bool) or (type(n2) == str or type(n2) == bool) or (type(n3) == str or type(n3) == bool):
        return Exception
    if type(tipo) != str or (tipo != 'A' and tipo != 'P'):
        return Exception
    if (n1 < 0 or n2 < 0 or n3 < 0) or (n1 > 10 or n2 > 10 or n3 >10):
        return Exception
    if tipo == 'A':
        media = round((n1 + n2 + n3) / 3, 1)
    else:
        media = round((n1 * 5 + n2 * 3 + n3 * 2) / 10, 1)
    
    return media  


assert calcular_media('2', 3, 4.5, 'A') == Exception
assert calcular_media(10, 3, 6, 'C') == Exception
assert calcular_media('P', 10, 3, 9) == Exception
assert calcular_media(10, 5, 8, False) == Exception
assert calcular_media(10, 3, -10, 'P') == Exception
assert calcular_media(0, 7, 12, 'A') == Exception
assert calcular_media(5, 7.6, 10, 3) == Exception
assert calcular_media(2.9, 3.5, 5.5, 'Ponderada') == Exception
assert calcular_media(2.9, 3.5, 5.5, 'a') == Exception
assert calcular_media(True, 4, 10, 'A') == Exception
assert calcular_media(2.9, 3.5, 5.5, 'P') == 3.6
assert calcular_media(2.9, 3.5, 5.5, 'A') == 4.0
assert calcular_media(4, 6, 8, 'A') == 6.0
assert calcular_media(4, 6, 8, 'P') == 5.4
assert calcular_media(0, 0, 0, 'A') == 0.0
assert calcular_media(0, 0, 0, 'P') == 0.0
assert calcular_media(10, 10, 10, 'A') == 10.0
assert calcular_media(10, 10, 10, 'P') == 10.0
print('Aprovada!!!')
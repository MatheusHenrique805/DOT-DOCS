'''10. Faça uma função que recebe a média final de um aluno por parâmetro e retorna o seu conceito, conforme a tabela abaixo:
            Nota          Conceito
        de 0,0 a 4,9         D
        de 5,0 a 6,9         C
        de 7,0 a 8,9         B
        de 9,0 a 10,0        A'''
def definir_conceito(media):
    if type(media) != float and type(media) != int:
        return Exception
    if media > 10 or media < 0:
        return Exception
    elif media >= 0 and media <= 4.9:
        conceito = 'D'
    elif media >= 5 and media <= 6.9:
        conceito = 'C'
    elif media >= 7 and media <= 8.9:
        conceito = 'B'
    else:
        conceito = 'A'
    
    return conceito    
    
    
assert definir_conceito(-1.0) == Exception
assert definir_conceito(-0.1) == Exception
assert definir_conceito(11.0) == Exception
assert definir_conceito('Dois vírgula 5') == Exception
assert definir_conceito(True) == Exception
assert definir_conceito(0.0) == 'D'
assert definir_conceito(0.1) == 'D'
assert definir_conceito(4.8) == 'D'
assert definir_conceito(4.9) == 'D'
assert definir_conceito(5) == 'C'
assert definir_conceito(5.1) == 'C'
assert definir_conceito(6.8) == 'C'
assert definir_conceito(6.9) == 'C'
assert definir_conceito(7) == 'B'
assert definir_conceito(7.1) == 'B'
assert definir_conceito(8.8) == 'B'
assert definir_conceito(8.9) == 'B'
assert definir_conceito(9) == 'A'
assert definir_conceito(9.1) == 'A'
assert definir_conceito(9.9) == 'A'
assert definir_conceito(10.0) == 'A'
print('Aprovada!!!')
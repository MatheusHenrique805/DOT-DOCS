'''8. Faça uma função que recebe um valor inteiro e verifica se o valor é positivo ou negativo. A função deve retornar um valor booleano.'''
def posivito_negativo(numero):
    if type(numero) != int or numero == 0:
        return Exception
    else:
        pass
    
    return 'Positivo' if numero > 0 else 'Negativo'


assert posivito_negativo('menos seis') == Exception
assert posivito_negativo(True) == Exception
assert posivito_negativo(0) == Exception
assert posivito_negativo(2.0) == Exception
assert posivito_negativo(1) == 'Positivo'
assert posivito_negativo(-1) == 'Negativo'
assert posivito_negativo(-13)== 'Negativo'
assert posivito_negativo(13)== 'Positivo'
print('Aprovada!!!')
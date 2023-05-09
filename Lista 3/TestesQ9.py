'''9. Faça uma função que recebe um valor inteiro e verifica se o valor é par ou ímpar. A função deve retornar um valor booleano.'''
def par_impar(n):
    if type(n) != int:
        return Exception
    else:
        pass
    
    return 'É par' if n % 2 == 0 else 'É impar'


assert par_impar('DEZ') == Exception
assert par_impar(21.5) == Exception
assert par_impar(True) == Exception
assert par_impar(1) == 'É impar'
assert par_impar(0) == 'É par'
assert par_impar(-1) == 'É impar'
assert par_impar(11) == 'É impar'
assert par_impar(2) == 'É par'
assert par_impar(335) == 'É impar'
print('Aprovada!!!')

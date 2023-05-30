'''5. Escreva uma função chamada "verificar_ano_bissexto" que receba um número inteiro como parâmetro e retorne True se o ano for bissexto, e False caso contrário. Um ano é
bissexto se for divisível por 4, mas não divisível por 100, exceto se for divisível por 400.'''
def verificar_ano_bissexto(ano):
    if type(ano) != int or ano == 0:
        return Exception
    else:
        if ano % 4 == 0 and ano % 100 != 0:
            return True
        elif ano % 4 == 0 and ano % 100 == 0 and ano % 400 == 0:
            return True
        elif ano % 4 != 0:
            return False
        elif ano % 4 == 0 and ano % 100 == 0 and ano % 400 != 0:
            return False
        else:
            return False



assert verificar_ano_bissexto('True') == Exception
assert verificar_ano_bissexto(True) == Exception
assert verificar_ano_bissexto(12.32) == Exception
assert verificar_ano_bissexto({}) == Exception
assert verificar_ano_bissexto(()) == Exception
assert verificar_ano_bissexto([]) == Exception
assert verificar_ano_bissexto(0) == Exception
assert verificar_ano_bissexto(2022)

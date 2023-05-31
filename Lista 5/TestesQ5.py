def verificar_ano_bissexto(ano):
    if (type(ano) != int) or (ano <= 3):
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
assert verificar_ano_bissexto(3) == Exception
assert verificar_ano_bissexto(4) == True
assert verificar_ano_bissexto(399) == False
assert verificar_ano_bissexto(400) == True
assert verificar_ano_bissexto(2022) == False
assert verificar_ano_bissexto(1004) == True
assert verificar_ano_bissexto(1005) == False
assert verificar_ano_bissexto(1000) == False
assert verificar_ano_bissexto(2024) == True
assert verificar_ano_bissexto(2032) == True
assert verificar_ano_bissexto(4000) == True
print('Testes OK!!!')

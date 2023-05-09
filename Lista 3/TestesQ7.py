'''7. Faça uma função que recebe a idade de um nadador por parâmetro e retorna a categoria desse nadador de acordo com a tabela abaixo:
                Idade     Categoria
            5 a 7 anos    Infantil A
            8 a 10 anos   Infantil B
            11-13 anos    Juvenil A
            14-17 anos    Juvenil B
            + 18 anos     Adulto
            (inclusive)          '''
def categorizar_idade(idade):
    if type(idade) != int or idade < 5:
        return Exception
    if idade >= 5 and idade <= 7:
        categoria = 'Infantil A'
    elif idade >= 8 and idade <= 10:
        categoria = 'Infantil B'
    elif idade >= 11 and idade <= 13:
        categoria = 'Juvenil A'
    elif idade >= 14 and idade <= 17:
        categoria = 'Juvenil B'
    else:
        categoria = 'Adulto'
    
    return categoria


assert categorizar_idade(0) == Exception
assert categorizar_idade(1) == Exception
assert categorizar_idade('cinco anos') == Exception
assert categorizar_idade(False) == Exception
assert categorizar_idade(-5) == Exception
assert categorizar_idade(3.5) == Exception
assert categorizar_idade(4) == Exception
assert categorizar_idade(5) == 'Infantil A'
assert categorizar_idade(6) == 'Infantil A'
assert categorizar_idade(7) == 'Infantil A'
assert categorizar_idade(8) == 'Infantil B'
assert categorizar_idade(9) == 'Infantil B'
assert categorizar_idade(10) == 'Infantil B'
assert categorizar_idade(11) == 'Juvenil A'
assert categorizar_idade(12) == 'Juvenil A'
assert categorizar_idade(13) == 'Juvenil A'
assert categorizar_idade(14) == 'Juvenil B'
assert categorizar_idade(16) == 'Juvenil B'
assert categorizar_idade(17) == 'Juvenil B'
assert categorizar_idade(18) == 'Adulto'
assert categorizar_idade(50) == 'Adulto'
assert categorizar_idade(69) == 'Adulto'
print('Aprovada!!!!')

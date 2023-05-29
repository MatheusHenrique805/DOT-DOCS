'''2. Crie uma função chamada "verificar_anagrama" que receba duas strings como parâmetros e retorne True se as duas strings forem anagramas (ou seja, possuírem as mesmas letras em quantidade igual, mas em ordem diferente), e False caso contrário.'''
def verificar_anagrama(str1, str2):
    if (type(str1) != str or type(str2) != str):
        return Exception
    if (len(str1) <= 0 or len(str2) <= 0):
        return Exception
    if str1.isalpha() == False or str2.isalpha() == False:
        return Exception
    else:
        if len(str1) == len(str2) and str1.lower() != str2.lower():
            for i in range(len(str1)):
                if str1[i].lower() not in str2.lower():
                    return False 
                else:
                    continue
        else:
            return False    
    return True
            
        
assert verificar_anagrama('', 'ralo') == Exception
assert verificar_anagrama(8, 56) == Exception
assert verificar_anagrama('', '') == Exception
assert verificar_anagrama(True, 'mostre') == Exception
assert verificar_anagrama(123.64, 'awsd') == Exception
assert verificar_anagrama('4345', '6544') == Exception
assert verificar_anagrama('o', 'arroba') == False
assert verificar_anagrama('roma', 'amor') == True
assert verificar_anagrama('amor', 'omar') == True
assert verificar_anagrama('america', 'iracema') == True
assert verificar_anagrama('sorte', 'morte') == False
assert verificar_anagrama('certo', 'torre') == False
assert verificar_anagrama('certo', 'torce') == True
assert verificar_anagrama('murro', 'muro') == False
assert verificar_anagrama('reto', 'terror') == False
assert verificar_anagrama('Morte', 'TERMO') == True
assert verificar_anagrama('TERMO', 'TERMO') == False 
print('Testes OK!!!')

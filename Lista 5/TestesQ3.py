'''3.Escreva uma função chamada "contar_caracteres" que receba uma string como parâmetro e retorne um dicionário onde as chaves são os caracteres encontrados na string e os valores são a quantidade de ocorrências de cada caractere.'''
def contar_caractere(string):
    if type(string) != str:
        return Exception
    else:
        registro_caractere = {}
        for i in range(len(string)):
            if string[i] not in registro_caractere:
                registro_caractere[string[i]] = 1
            else:
                registro_caractere[string[i]] += 1
            
    return registro_caractere

assert contar_caractere('') == Exception
assert contar_caractere(0) == Exception
assert contar_caractere(False) == Exception
assert contar_caractere(12.43) == Exception
assert contar_caractere('Matheus') == ({'M': 1, 'a': 1, 't': 1, 'h': 1, 'e': 1, 'u': 1, 's': 1})
assert contar_caractere('Amar') == ({'A': 1, 'm': 1, 'a': 1, 'r': 1})
assert contar_caractere('João') == ({'J': 1, 'o': 2, 'ã': 1})
assert contar_caractere('Mamona') == ({'M': 1, 'a': 2, 'm': 1, 'o': 1, 'n': 1})
assert contar_caractere('Mama') == ({'M': 1, 'a': 2, 'm': 1})
assert contar_caractere('1267') == ({'1': 1, '2': 1, '6': 1, '7': 1})
assert contar_caractere(' ') == ({' ': 1})
assert contar_caractere('"@#$#@#$$##') == ({'"': 1, '@': 2, '#': 5, '$': 3})
print('Testes OK!!!')
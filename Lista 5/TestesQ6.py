'''6. Crie uma função chamada "contar_substrings" que receba uma string e uma substring como parâmetros e retorne a quantidade de ocorrências da substring na string'''
def contar_substrings(string, substring):
    if type(string) != str or type(substring) != str:
        return Exception
    if len(string) == 0 or len(substring) == 0:
        return Exception
    if len(string) < len(substring) or len(string) == len(substring):
        return Exception
    else:
        contagem = 0
        for i in range(len(string)):
            if string[i:i + len(substring)] == substring:
                contagem += 1
            else:
                continue
    
    return contagem


assert contar_substrings('', '') == Exception
assert contar_substrings(1, '123') == Exception
assert contar_substrings('assim', True) == Exception
assert contar_substrings('12.4', 12.4) == Exception
assert contar_substrings('senso', []) == Exception
assert contar_substrings((), 'tup') == Exception
assert contar_substrings({}, 'dicio') == Exception
assert contar_substrings('pro', 'assopro') == Exception
assert contar_substrings('inchaço', 'inchaço') == Exception
assert contar_substrings('caco', 'dado') == Exception
assert contar_substrings('121432134233', '12') == 1 
assert contar_substrings('caCO', 'c') == 1
assert contar_substrings('bebida azeda', 'da') == 2
assert contar_substrings('Inteligência Artificial', 'cia') == 2
assert contar_substrings('in-te-li-gên-cia', '-') == 4
assert contar_substrings('hipocondríaco', 'Condriaco') == 0 
assert contar_substrings('banana', 'nA') == 0 
assert contar_substrings('banana', 'na') == 2
assert contar_substrings('O rato roeu a roupa do rei de Roma.', 'na') == 0 
assert contar_substrings('O rato roeu a roupa do rei de Roma.', ' ') == 8 
print('Testes OK!!!')
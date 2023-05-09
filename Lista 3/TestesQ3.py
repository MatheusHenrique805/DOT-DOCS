'''3. Faça uma função que recebe por parâmetro um valor inteiro e positivo e retorna o valor lógico Verdadeiro caso o valor seja primo e Falso em caso contrário'''
def verificar_primo(n):
    if type(n) != int or n <= 0:
        return Exception
    else:
        valores = []
        for valor in range(1, n + 1):
            if n % valor == 0:
                valores.append(valor)
            else:continue
                
    return 'É primo' if len(valores) == 2 else 'Não é primo'


assert verificar_primo('abc') == Exception
assert verificar_primo(1.0) == Exception
assert verificar_primo(False) == Exception
assert verificar_primo(0) == Exception
assert verificar_primo(-1) == Exception
assert verificar_primo(1) == 'Não é primo'
assert verificar_primo(2) == 'É primo'
assert verificar_primo(3) == 'É primo'
assert verificar_primo(4) == 'Não é primo'
assert verificar_primo(11) == 'É primo'
print('Aprovada!!!')
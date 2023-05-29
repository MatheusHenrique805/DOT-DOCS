'''8. Crie uma função chamada "remover_vogais" que receba uma string como parâmetro e retorne uma nova string sem as vogais.'''
def remover_vogais(string):
    if type(string) != str:
        return Exception
    if len(string) == 0:
        return Exception
    else:
        vogais = 'AÃÁÀÂaãàâEÊÉeêéIÍÎiîíOÕÓÔoôõóUÚÛuúû'
        strng = ''
        for letra in string:
            if letra not in vogais:
                strng += letra
            else:
                continue
    
    return strng


assert remover_vogais('') == Exception
assert remover_vogais(12) == Exception
assert remover_vogais(True) == Exception
assert remover_vogais(12.3) == Exception
assert remover_vogais(' ') == (' ')
assert remover_vogais('1232423') == ('1232423')
assert remover_vogais('A435S760O') == ('435S760')
assert remover_vogais('Matheus') == ('Mths')
assert remover_vogais('ExCesso') == ('xCss')
assert remover_vogais('BanAna') == ('Bnn')
assert remover_vogais('matheushenry21@gmail.com') == ('mthshnry21@gml.cm')
assert remover_vogais('aaaaaaaaaaaaaaaaaaaaaaaai') == ('')
print('Testes OK!!!')
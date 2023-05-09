'''Q4. Escreva um programa para ler as notas das duas avaliações de um aluno no semestre. Faça um procedimento que receba as duas notas por parâmetro e calcule e escreva a média semestral e a mensagem “PARABÉNS! Você foi aprovado!” somente se o aluno foi aprovado (considere 6.0 a média mínima para aprovação)'''

def media_semestre(n1, n2):
    msg = f''
    med = (n1 + n2) / 2
        
    if med >= 6:
        msg = f'{med:.1f}, PARABÉNS! Você foi aprovado!'
    else:
        msg = f'{med:.1f}, Você não foi aprovado :(.'
        
    return msg


def main():
    keep_running = True
    
    while keep_running:
        try:
            nota1 = float(input('Digite a primeira nota do semestre.\n'))
            nota2 = float(input('Agora sua segunda nota do semestre.\n'))
                    
            media_msg = media_semestre(nota1, nota2)
                
            print(f'{media_msg}')
            break
        except ValueError:
            print('Não digite nada diferente de algarismos e ponto')
                
    
if __name__ == '__main__':
    main()
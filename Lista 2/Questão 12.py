'''12) Deseja-se publicar o número de acertos de cada aluno em uma prova em forma de testes. A prova consta de 30 questões, cada uma com cinco alternativas identificadas por A, B, C, D e E. Para isso são dados:
    o cartão gabarito;
    o número de alunos da turma;
    o cartão de respostas para cada aluno, contendo o seu número e suas respostas'''
def publicar_acertos(lista_gabarito, lista_cartao):
    saida_acertos = f''
    for i in range(len(lista_cartao)):
        acertos = 0
        for c in range(len(lista_gabarito)):
            if lista_cartao[i][c] == lista_gabarito[c]:
                acertos += 1
            else:
                continue
            
        saida_acertos += f'O aluno {i+1} teve {acertos} acertos\n'
    
    return saida_acertos


def coletar_respostas(lista_gabarito):
    while True:
        try:
            qtd_candit = int(input('Quantos candidatos são?\n'))
            lista_candidatos = [] 
            print('Digitar as',len(lista_gabarito),'respostas de cada candidadto.')
            for i in range(qtd_candit):
                lista_respostas = []
                for c in range(len(lista_gabarito)):
                    escolha = input(f'Candidato {i+1}; Questão {c+1}.\n ').upper()
                    if escolha in 'ABCDE':
                        lista_respostas.append(escolha)
                    else:
                        while escolha not in 'ABCDE':
                            escolha = input(f'Só é aceito A, B, C, D ou E como resposta!!!\nDigite novamente.\n').upper()
                            if escolha in 'ABCDE':
                                lista_respostas.append(escolha)
                            else:
                                continue
                lista_candidatos.append(lista_respostas)
            break
        except:
            print('DADO INCOERENTE!!!')
            
    return lista_candidatos


def main():
    while True:
        try:
            lista_gabarito = []
            for i in range(30):
                resposta = input(f'Digite o gabarito da {i+1}º questão.\n').upper()
                if resposta == 'A' or resposta == 'B' or resposta == 'C' or resposta == 'D' or resposta == 'E':
                    lista_gabarito.append(resposta)
                else:
                    while resposta not in 'ABCDE':
                        resposta = input('Só é aceito A, B, C, D ou E como gabarito!!\nDigite novamente.\n').upper()
                        if resposta in 'ABCDE':
                            lista_gabarito.append(resposta)
                        else:
                            pass
            
            lista_cartao = coletar_respostas(lista_gabarito)
            
            print(publicar_acertos(lista_gabarito, lista_cartao))
            break
        except:
            print('ERRO!!')
    
if __name__ == '__main__':
    main()
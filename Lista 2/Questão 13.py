'''13) Tentando descobrir se um dado era viciado, um dono de cassino honesto (ha! ha! ha! ha!) o
lançou n vezes. Dados os n resultados dos lançamentos, determinar o número de ocorrências de cada face. '''
from random import randint

def contar_ocorenface(results,l):
    face1 = face2 = face3 = face4 = face5 = face6 = 0
    ocorre = f''
    for resultado in results:
        if resultado == 1:
            face1 += 1
        elif resultado == 2:
            face2 += 1
        elif resultado == 3:
            face3 += 1
        elif resultado == 4:
            face4 += 1
        elif resultado == 5:
            face5 += 1
        else:
            face6 += 1

    ocorre = f'face 1:{face1}/{l}\nface 2:{face2}/{l}\nface 3:{face3}/{l}\nface 4:{face4}/{l}\nface 5:{face5}/{l}\nface 6:{face6}/{l}'
    
    return ocorre


def lancar_dado(n_lanc):
    results = []
    
    for _ in range(n_lanc):
        resultado = randint(1,6)
        results.append(resultado)
    
    ocorrencias_face = contar_ocorenface(results, n_lanc)

    return ocorrencias_face

        
def main():
    while True:
        try:
            n_lancamentos = int(input('Quantos lançamentos vão ser?\n'))
            
            if n_lancamentos != 0 and n_lancamentos > 0:
                ocorrencias_face = lancar_dado(n_lancamentos)
                print('Ocorrências das faces do dado(/ total de lançamentos):')
                print(ocorrencias_face)
                break    
            else:
                raise ValueError
        except ValueError:
            print('INFORMAÇÃO INVÁLIDA!!')

if __name__ == '__main__':
    main()
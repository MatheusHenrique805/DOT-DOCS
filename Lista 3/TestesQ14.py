'''14. Escreva uma função que recebes 3 valores reais X, Y e Z e que verifique se esses valores podem ser os comprimentos dos lados de um triângulo e, neste caso, retornar qual o tipo de triângulo formado. Para que X, Y e Z formem um triângulo é necessário que a seguinte propriedade seja satisfeita: o comprimento de cada lado de um triângulo é menor do que a soma do comprimento dos outros dois lados. O procedimento deve identificar o tipo de triângulo formado observando as seguintes definições:
            o Triângulo Equilátero: os comprimentos dos 3 lados são iguais.
            o Triângulo Isósceles: os comprimentos de 2 lados são iguais.
            o Triângulo Escaleno: os comprimentos dos 3 lados são diferentes.'''
def classificar_triangulo(x, y, z):
    if (type(x) != int and type(x) != float) or (type(y) != int and type(y) != float) or (type(z) != int and type(z) != float):
        return Exception
    if (x == y == z == 0) or (x <= 0 or y <= 0 or z <= 0):
        return Exception
    if (x >= y + z) or (y >= x + z) or (z >= x + y):
        return Exception
    if x != y and x != z and y != z:
        classif = 'Triângulo Escaleno'
    elif (x == y and x != z) or (y == z and y != x) or (z == x and z != y):
        classif = 'Triângulo Isósceles'
    elif x == y == z:
        classif = 'Triângulo Equilátero'
    else:
        pass

    return classif


assert classificar_triangulo('abc', 21, 12) == Exception
assert classificar_triangulo(-12, 20, -31) == Exception
assert classificar_triangulo(0,0, 143) == Exception
assert classificar_triangulo(True, False, 20.3) == Exception
assert classificar_triangulo(2, 1, 1) == Exception
assert classificar_triangulo(12.5, 1.5, 5.8) == Exception
assert classificar_triangulo(2, 1, 3) == Exception
assert classificar_triangulo(1, 1, 1) == 'Triângulo Equilátero' 
assert classificar_triangulo(3, 4, 5) == 'Triângulo Escaleno'
assert classificar_triangulo(60, 30, 60) == 'Triângulo Isósceles'
assert classificar_triangulo(12.1, 12.1, 23.4) == 'Triângulo Isósceles'
assert classificar_triangulo(23, 12, 12) == 'Triângulo Isósceles'
assert classificar_triangulo(21.5, 34.1, 22.1) == 'Triângulo Escaleno'
assert classificar_triangulo(7.5, 2.9, 7.5) == 'Triângulo Isósceles'
assert classificar_triangulo(2.5, 2.5, 2.5) == 'Triângulo Equilátero'
print('Função aprovada!!!')
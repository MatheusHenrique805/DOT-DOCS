'''Q3. Escreva um programa para ler uma temperatura em graus Fahrenheit. Faça uma função chamada celsius para calcular e retornar o valor correspondente em graus Celsius.
        Fórmula: C = ((F-32)/9)*5'''

def celsius(tf):
    return ((tf - 32) / 9) * 5
    

def main():
    keep_running = True
    
    while keep_running:
        try:
            tempf = float(input('Digite uma temperatura em graus Fahrenheith.\n'))
            
            tempc = celsius(tempf)

            print(f'{tempf}°F equivale a {tempc:.2f}°C')
            break
        except ValueError:
            print('Digite somente o valor da temperatura')
    

if __name__ == '__main__':
    main()
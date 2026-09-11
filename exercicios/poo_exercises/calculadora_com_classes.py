from classes import Calculadora

def main():
    print('---- Bem vindo a calculadora com classes ----')
    calculadora = Calculadora(923, '+', 57)
    print(f"Resultado: {calculadora.calcular()}")
    print()
    return

if __name__ == '__main__':
    main()
from rich import print, inspect
from classes import *

def main():
    polig = Circulo(int(input('Digite um valor: ')))
    
    print(f'Perimetro: {polig.perimetro():.1f} | Area: {polig.area():.1f}')

if __name__ == '__main__':
    main()
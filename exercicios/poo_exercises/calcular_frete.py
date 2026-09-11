from classes import *

def main():
    distancia = 20

    entrega = Moto(distancia)
    print(f'\nFrete de {type(entrega).__name__} em {distancia}Km = {entrega.calc_frete()}\n')

if __name__ == '__main__':
    main()
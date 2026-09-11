from classes import Diario
from rich import inspect

def main():
    seg1 = Diario()
    seg1.anotar_algo('Adoro doces')
    seg1.anotar_algo('Gosto de filmes românticos')
    seg1.anotar_algo('Python é demais!')
    
    seg1.ler_conteudo()
    return

if __name__ == '__main__':
    main()
from classes import *
from rich import inspect
from rich.panel import Panel
from rich import print as rprint

def main():
    print()
    f1 = Pedreiro('Cleber', 12, 200)
    Relatorio.exibir(f1)
 
    f2 =  Professor('Jorge', 8000)
    Relatorio.exibir(f2)
    print()
    return

if __name__ == '__main__':
    main()
from classes import Termostato
from rich import inspect

def main():
    t = Termostato()
    print()
    t.ftemperatura
    t.temperatura = 20
    t.ftemperatura
    t.temperatura = 25.5
    t.ftemperatura
    t.temperatura = 17.5
    t.ftemperatura
    print()
    
    # inspect(t, private=True, methods=True)
    return

if __name__ == '__main__':
    main()
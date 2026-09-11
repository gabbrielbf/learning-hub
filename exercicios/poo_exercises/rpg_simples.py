from classes import *

def main():
    p1 = Guerreiro('Battle Beast',  4500)
    p2 = Mago('Gandolf',  2300)

    print()
    p1.atacar(p2, 1000)
    print()
    p2.curar()
    print()
    p2.atacar(p1, 2000)
    print()
    p1.curar()
    print()

if __name__ == '__main__':
    main()
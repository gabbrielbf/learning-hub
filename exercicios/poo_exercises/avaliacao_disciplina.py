from classes import Avaliacao
from rich import print, inspect

def main():
    av1 = Avaliacao('João', 'Física', 8.7)
    print(f'{av1.nome} tirou {av1._nota} em {av1.disciplina}.')
    av1.set_nota(5.4)
    print(f'{av1.nome} tirou {av1._nota} em {av1.disciplina}.')
    inspect(av1)
    return

if __name__ == '__main__':
    main()
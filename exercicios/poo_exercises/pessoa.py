from classes import Aluno
from rich import inspect

def main():
    print('='*40)
    print('Criando e instânciando aluno')
    print('='*40)

    josue = Aluno('Josué', 2002)
    print(f'\nJosué nasceu no ano: {josue._nascimento}')
    print(f'Sua idade atual é: {josue.idade} anos')
    print(f'Os cursos disponíveis e atuais são: {josue.lista_cursos}')
    josue.add_curso('eng') # <- Colocando de propósito em caracteres minúsculos para testar validação e adição
    josue.add_curso('adv') # <- Colocando este curso para usa-lo posteriormente
    print(f'Os cursos disponíveis e atuais AGORA são: {josue.lista_cursos}')
    print(f'Seu curso atual é: {josue._curso}')
    josue.curso = 'adv'
    print(f'Seu curso atual é: {josue._curso}\n')
    return

if __name__ == '__main__':
    main()
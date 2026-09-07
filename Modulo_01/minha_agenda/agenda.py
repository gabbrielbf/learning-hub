import os
import time

def exibir_agenda():
    """ Função de exibição do menu """

    print(('-'* 4) + 'Minha agenda' + ('-' * 4))
    print('O que deseja fazer: ')
    print('1 - Salvar contato')
    print('2 - Editar contato')
    print('3 - Deletar contato')
    print('4 - Marcar um contato como favorito')
    print('5 - Exibir lista de favoritos')
    print('0 - Sair')
    print('-' * 20)
    opcao = int(input('Digite uma das opções acima: '))
    return opcao


def encerrar_ou_continuar():
    """ Função para opcionar o usuário 
    a continuar ou encerrar ou encerrar o programa """

    print()
    print('O que deseja fazer agora: ')
    print('-' * 20)
    print('1 - Voltar ao MENU ')
    print('0 - Encerrar o programa ')
    print('-' * 20)
    while True:
        try:
            encerrar = int(input('Digite aqui -> '))
        except ValueError:
            print('[ERRO]! Você digitou algo inválido.')
            print()
            continue
        if encerrar == 1:
            print('Vamos continuar então!\n')
            time.sleep(0.7)
            encerrar = False
            break
        elif encerrar == 0:
            print('Encerrando programa.\n')
            time.sleep(0.7)
            encerrar = True
            break
        else:
            print('Opção inválida!\nTente novamente ')
            continue
    return encerrar
        

def adicionar_contato(nome, telefone, email):
    """ Função para adicionar um contato """

    minha_agenda.append({'nome': nome, 'telefone': telefone,
                          'email': email, 'favorito': False})
    print()
    print(f'Contato: {nome} | {telefone} adicionado com sucesso!')
    return


def adicionar_mais_alguem():
    """ Função para definir se o usuário quer
    continuar adicionando pessoas. """

    print()
    print('-' * 20)
    print('1 - Adicionar mais alguém')
    print('0 - Voltar ao MENU')
    print('-' * 20)
    while True:
        try:
            adicionar_outro = int(input('Deseja adicionar mais alguém? '))
        except ValueError:
            print('Opção inválida.')
            print()
            continue
        match adicionar_outro:
            case 1:
                adicionar_outro = True
                break
            case 0:
                adicionar_outro = False
                break
            case _:
                print('Opção inválida.')
                print()
                continue

    return adicionar_outro


def visualizar_contatos(agenda):
    print('Estes são seus contatos: ')
    for indice, contato in enumerate(minha_agenda, start=1):
        favorito = '❤️ ' if contato['favorito'] else ' '
        nome_contato = contato['nome']
        numero_contato = contato['telefone']
        email_contato = contato['email']
        print(f'{indice} - [{favorito}] | Nome: {nome_contato} | Número: {numero_contato} | E-mail: {email_contato}')
    print()
    return 


def visualizar_favoritos(agenda):
    print('Estes são seus contatos favoritados: ')
    for indice, contato in enumerate(minha_agenda, start=1):
        favorito = '❤️ ' if contato['favorito'] else ' '
        nome_contato = contato['nome']
        numero_contato = contato['telefone']
        email_contato = contato['email']
        if contato['favorito']:
            print(f'{indice} - [{favorito}] | Nome: {nome_contato} | Número {numero_contato} | E-mail: {email_contato}')
        # else:
        #     print('Você não tem contatos favoritos!')
    return


def editar_somente_nome(agenda, indice_contato, nome):
    """ Função designada apenas para edição de nome do usuário """

    indice_contato_correto = indice_contato - 1
    if indice_contato_correto >= 0 and indice_contato_correto < len(minha_agenda):
        agenda[indice_contato_correto]['nome'] = nome
        print(f'Contato {indice_contato} atualizado com sucesso!')
    else:
        print('[ERRO]! O Indice é inválido!')
        print()
    return
    

def editar_somente_telefone(agenda, indice_contato, telefone):
    """ Função designada apenas para edição de telefone do usuário """

    indice_contato_correto = indice_contato - 1
    if indice_contato_correto >= 0 and indice_contato_correto < len(minha_agenda):
        agenda[indice_contato_correto]['telefone'] = telefone
        print(f'Contato {indice_contato} atualizado com sucesso!')
    else:
        print('[ERRO]! O Indice é inválido!')
        print()
    return


def editar_somente_email(agenda, indice_contato, email):
    """ Função designada apenas para edição de e-mail do usuário """

    indice_contato_correto = indice_contato - 1
    if indice_contato_correto >= 0 and indice_contato_correto < len(minha_agenda):
        agenda[indice_contato_correto]['email'] = email
        print(f'Contato {indice_contato} atualizado com sucesso!')
    else:
        print('[ERRO]! O Indice é inválido!')
        print()
    return
    

def editar_contato(agenda, indice_contato, nome, telefone, email):
    """ Função designada para edição de todos os dados do usuário """

    indice_contato_correto = indice_contato - 1
    if indice_contato_correto >= 0 and indice_contato_correto < len(minha_agenda):
        agenda[indice_contato_correto]['nome'] = nome
        agenda[indice_contato_correto]['telefone'] = telefone
        agenda[indice_contato_correto]['email'] = email
        print(f'Contato {indice_contato} atualizado com sucesso!')
    else:
        print('[ERRO]! O Indice é inválido!')
        print()
    return 


def deletar_contato(agenda, indice_contato):
    """ Função designada apenas para deletar contatos """

    indice_contato_correto = indice_contato - 1

    for contato in range(len(agenda)):
        if indice_contato_correto == contato:
            minha_agenda.remove(minha_agenda[contato])
            break

    print(f'O contato de indice {indice_contato} foi removido!')

    return 


def favoritar_contato(agenda, indice_contato):
    """ Função designada para favoritar um usuário """
    
    indice_contato_correto = indice_contato - 1
    agenda[indice_contato_correto]['favorito'] = True
    print(f'O contato {indice_contato} foi favoritado com sucesso!')
    return

minha_agenda = []

while True:
    os.system('cls')
    match exibir_agenda():
        case 0:
            print()
            print('Programa encerrado...')
            print()
            time.sleep(0.7)
            break
        case 1:
            while True:
                try:
                    nome = str(input('Digite o nome do contato: ')).title()
                    telefone = int(input('Digite o telefone do contato: '))
                    email = input('Digite o e-mail do contato: ')
                except ValueError:
                    print('[ERRO]! Você digitou algo inválido.')
                    print()
                    continue
                adicionar_contato(nome, telefone, email)

                if adicionar_mais_alguem() == True:
                    continue
                else:
                    print('Voltando para o menu...')
                    print()
                    break
        case 2:
            if minha_agenda == []:
                print('Você ainda não adicionou ninguém!')
                time.sleep(0.7)
                print()
                continue
            else:
                visualizar_contatos(minha_agenda)
                while True:
                    try:
                        indice_contato = int(input('Qual contato deseja editar: '))
                    except ValueError:
                        print('[ERRO]! Você digitou algo inválido.')
                        print()
                        continue
                    break
                print('-' * 20)
                print('Qual dado abaixo deseja atualizar: ')
                print('-' * 20)
                print('1 - Nome')
                print('2 - Telefone')
                print('3 - E-mail')
                print('4 - Todos os dados')
                print('-' * 20)

                while True:
                    try:
                        qual_dado_atualizar = int(input('Digite aqui -> '))
                    except ValueError:
                        print('[ERRO]! Você digitou algo inválido.')
                        print()
                        continue
                    match qual_dado_atualizar:
                        case 1:
                            while True:
                                try:
                                    novo_nome = str(input('Digite o nome desejado: ')).title()
                                except ValueError:
                                    print('[ERRO]! Você digitou algo inválido.')
                                    print()
                                    continue
                                break
                            editar_somente_nome(minha_agenda, indice_contato, novo_nome)
                            break
                        case 2:
                            while True:
                                try:
                                    novo_contato = int(input('Digite o CONTATO desejado: '))
                                except ValueError:
                                    print('[ERRO]! Você digitou algo inválido.')
                                    print()
                                    continue
                                break
                            editar_somente_telefone(minha_agenda, indice_contato, novo_contato)
                            break
                        case 3:
                            while True:
                                try:
                                    novo_email = input('Digite o E-MAIL desejado: ')
                                except ValueError:
                                    print('[ERRO]! Você digitou algo inválido.')
                                    print()
                                    continue
                                break
                            editar_somente_email(minha_agenda, indice_contato, novo_email)
                            break
                        case 4:
                            while True:
                                try:
                                    novo_nome = str(input('Digite o NOME desejado: ')).title()
                                    novo_contato = int(input('Digite o CONTATO desejado: '))
                                    novo_email = input('Digite o E-MAIL desejado: ')
                                except ValueError:
                                    print('[ERRO]! Você digitou algo inválido.')
                                    print()
                                    continue
                                break
                            editar_contato(minha_agenda, indice_contato, novo_nome, novo_contato, novo_email)
                            break
                        case _:
                            print('Digite uma das opções acima!')
                            print()
                            continue
                if encerrar_ou_continuar() == False:
                    continue
                else:
                    break          
        case 3:
            if minha_agenda == []:
                print('Você ainda não adicionou ninguém!')
                time.sleep(0.7)
                print()
                continue
            else:
                visualizar_contatos(minha_agenda)
                while True:
                    try:
                        indice_contato = int(input('Digite o INDICE de qual deseja deletar: '))
                    except ValueError:
                        print('[ERRO]! Você digitou algo inválido.')
                        print()
                        continue
                    break
                deletar_contato(minha_agenda, indice_contato)

                if encerrar_ou_continuar() == False:
                    continue
                else:
                    break
        case 4:
            if minha_agenda == []:
                print('Você ainda não adicionou ninguém!')
                time.sleep(0.7)
                print()
                continue
            else:
                visualizar_contatos(minha_agenda)
                while True:
                    try:
                        indice_contato = int(input('Qual contato deseja favoritar: '))
                    except ValueError:
                        print('[ERRO]! Você digitou algo inválido.')
                        print()
                        continue
                    break
                favoritar_contato(minha_agenda, indice_contato)

                if encerrar_ou_continuar() == False:
                    continue
                else:
                    break
        case 5:
            if minha_agenda == []:
                print('Você ainda não adicionou ninguém!')
                time.sleep(0.7)
                print()
                continue
            else:
                visualizar_favoritos(minha_agenda)
                time.sleep(1.5)

                if encerrar_ou_continuar() == False:
                    continue
                else:
                    break
        case _:
            print('Opção não está disponível\nTente novamente.')
            print()
            continue
    time.sleep(0.9)
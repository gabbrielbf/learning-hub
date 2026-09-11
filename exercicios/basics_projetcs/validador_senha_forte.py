def validar_senha(senha):
    if len(senha) >= 8:
        for caractere in senha:
            if caractere in ('0123456789'):
                return True
    return False

while True:

    senha = input('Digite a senha: ')

    if validar_senha(senha) == True:
        print('senha válida.')
        break
    else:
        print('senha inválida')
        continue

print('\nprograma finalizado\n')
    


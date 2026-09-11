import os, time

# Sistema de inventário de loja
estoque = []

def limpar_interface():
    os.system('cls' if os.name == 'nt' else 'clear')
    return

def exibir_menu():
    print('-'*30)
    print('1 - adicionar produto')
    print('2 - visualizar estoque')
    print('3 - vender produto')
    print('4 - repor produto')
    print('0 - sair')
    print('-'*30)
    while True:
        try:
            opcao = int(input('digite a opcao -> '))
        except ValueError:
            print('[ERRO] valor inválido')
            continue
        if opcao not in range(0, 5):
            print('[ERRO] digite um valor dentre [0 e 4]')
            continue
        else:
            break
    return opcao
    
def inserir_produto(nome:str, preco:float, qtd_estoque:int):
    estoque.append({'nome':nome, 'preco':preco, 'qtd_estoque':qtd_estoque})
    print(f'o produto {nome} foi adicionado com sucesso ✔️')
    return

def exibir_estoque():
    print('-'*30)
    for indice, produto in enumerate(estoque, start=1):
        print(f'produto {indice} - {produto['nome']:<8} | preço {produto['preco']:<4} | estoque {produto['qtd_estoque']}')
    print('-'*30)
    return

def vender_produto(venda:str, quantidade:int):
    
    valor_compra = 0.0

    encontrado = False
    for indice, item in enumerate(estoque):
        if venda == item['nome']:
            encontrado = True
            break
        else:
            continue

    for indice, item in enumerate(estoque):
        if venda == item['nome']:
            if (item['qtd_estoque'] <= 0 or 
                quantidade > item['qtd_estoque']):
                raise Exception('estoque insuficiente.')
            else:
                valor_compra += (item['preco'] * quantidade)
                item['qtd_estoque'] -= quantidade
                if item['qtd_estoque'] < 0:
                    item['qtd_estoque'] = 0 # <- Essa linha de código foi criada puramente para exibir '0'
                                                        # quando o usuário selecionar a opção 2 no menu inicial
                print(f'você comprou {quantidade} unidades de {item['nome']} e o valor deu: {valor_compra}')

    return encontrado

def repor_produto(produto:str, quantidade:int):

    encontrado = False
    for indice, item in enumerate(estoque):
        if produto == item['nome']:
            encontrado = True
            break
        else:
            continue
        
    if encontrado == False:
        raise Exception('produto não encontrado.')

    if quantidade <= 0:
        raise Exception('digite um valor maior que zero!')
    
    for indice, item in enumerate(estoque):
        if produto == item['nome']:
            item['qtd_estoque'] += quantidade
            print(f'estoque atualizado com sucesso ✔️\no produto {item['nome']} agora possui {item['qtd_estoque']} itens.')

    return encontrado

def main():
    while True:
        limpar_interface()
        match exibir_menu():
            case 1:
                while True:
                    try:
                        nome_produto = str(input('digite o nome do produto: ')).title().strip()
                        preco_produto = float(input('digite o preço do produto: '))
                        qtd_produto = int(input('quantidade inicial do produto: '))
                    except ValueError:
                        print('[ERRO] valor digitado inválido.')
                        print()
                        continue
                    inserir_produto(nome_produto, preco_produto, qtd_produto)
                    break
            case 2:
                if not estoque:
                    print('[ERRO] estoque vazio!')
                    time.sleep(0.8)
                    continue
                exibir_estoque()
            case 3:
                if not estoque:
                    print('[ERRO] estoque vazio!')
                    time.sleep(0.8)
                    continue
                exibir_estoque()
                while True:
                    try:
                        venda = str(input('o que deseja comprar -> ')).title().strip()
                        quantidade = int(input('quantas un. deseja comprar -> '))
                    except ValueError:
                        print('valor digitado inválido.')
                        continue
                    
                    if vender_produto(venda, quantidade) == False:
                        print('[ERRO] produto não encontrado')
                        print()
                    else:
                        break
            case 4:
                if not estoque:
                    print('[ERRO] estoque vazio!')
                    time.sleep(0.8)
                    continue
                exibir_estoque()
                while True:
                    try:
                        produto = str(input('qual produto deseja repor da lista acima -> ')).title().strip()
                        quantidade = int(input('quantas un. deseja repor -> '))
                    except ValueError:
                        print('[ERRO] valor digitado inválido.')
                    if repor_produto(produto, quantidade) ==  False:
                        print('[ERRO] produto não encontrado')
                        print()
                    else:
                        break
            case 0:
                print('\nencerrando...\n')
                break
        time.sleep(2)

if __name__ == '__main__':
    main()


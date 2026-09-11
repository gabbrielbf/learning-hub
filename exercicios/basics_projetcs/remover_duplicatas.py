def remover_duplicatas(lista_original):
    lista_limpa = []
    nomes_vistos = []
    
    for nome in lista_original:
        nome_minusculo = nome.lower()
        
        if nome_minusculo not in nomes_vistos:

            lista_limpa.append(nome)
            nomes_vistos.append(nome_minusculo)
            
    return lista_limpa

lista_original = ['Maria', 'joao','João', 'Lucio', 'maria', 'ana','Jorge', 'Ana', 'jorge']
resultado = remover_duplicatas(lista_original)

print(resultado)
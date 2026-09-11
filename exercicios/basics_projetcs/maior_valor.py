import random

def conferir_maior(lista_valores):
    maior_valor = lista_valores[0]
    for valor in lista_valores:
        if valor > maior_valor:
            maior_valor = valor
        else:
            continue
    return maior_valor

lista_valores = []

for numero in range(1, 16): # <- responsável por evitar o trabalho braçal de adicionar um numero por vez a lista de valores
    valor = random.randint(1, 100) # <-  adicionando 15 valores aleatórios
    lista_valores.append(valor)

maior_valor = conferir_maior(lista_valores)
print(maior_valor)

import random

def separar_pares_e_impares(lista_numeros):
    lista_pares = []
    lista_impares = []

    for numero in lista_numeros:
        if numero % 2 == 0:
            lista_pares.append(numero)
        else:
            lista_impares.append(numero)

    return lista_pares, lista_impares

lista_numeros = []

for numero in range(0, 51):
    valor = random.randint(1, 101)
    lista_numeros.append(valor)
lista_pares, lista_impares = separar_pares_e_impares(lista_numeros)

print(f'lista de pares: {lista_pares}')
print(f'lista de impares: {lista_impares}')
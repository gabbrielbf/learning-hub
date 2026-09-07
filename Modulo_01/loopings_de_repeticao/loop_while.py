while True:
    print("\nMenu do Gerenciador de Lista de tarefas:")
    print("1. Adicionar tarefa")
    print("2. Ver tarefas")
    print("3. Atualizar Tarefas")
    print("4. Completar Tarefas")
    print("5. Deletar tarefas completadas")
    print("6. Sair")

    escolha = input("Digite a sua escolha: ")

    if escolha == "6":
        break

print("Programa finalizado")

# Exemplo de While

print("Exemplo de while")
contador = 0
while True:
    print("Contagem:", contador)
    contador += 1
    if contador == 5:
        break

print("Programa finalizado")

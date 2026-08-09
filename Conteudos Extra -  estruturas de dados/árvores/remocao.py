# Implementando os três casos de remoção dos nós de uma Árvore Binária de Busca

from binary_search_tree import BinarySearchTree

def extanded_tree(): # função criada para realizar a inserção de uma determinada lista de valores similar a lista do arquivo tree_concepts.py
                     # e fazer uma remoção dinâmica
    values = [61, 89, 66, 43, 51, 16, 55, 11, 79, 77, 82, 32, 100, 90]
    tree = BinarySearchTree()

    for value in values:
        tree.insert(value)
    return tree

# testando remoção

print('\n')
binary_search_tree = extanded_tree()
binary_search_tree.inorder_search()

value = 61
binary_search_tree.remove(value)

print('\n')
print(f'Após remover -> {value}')
binary_search_tree.inorder_search()

print('\n')

binary_search_tree.levelorder_search()

print('\n')

print('Máximo:', binary_search_tree.search_max())
print('Mínimo:', binary_search_tree.search_min())

print('\n')

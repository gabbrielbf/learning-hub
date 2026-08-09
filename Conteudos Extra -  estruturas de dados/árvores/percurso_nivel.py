# Para esse projeto em específico, iremos trabalhar com uma outra estrutura de dados, porém linear, chamada Fila. Que se trata de remover o 
# primeiro item a entrar na mesma, e isso é justamente o que o percurso em nível faz! O primeiro item (no caso a raiz) é o primeiro a sair
# seguindo assim essa mesma metodologia para seus filhos.

# from queue import Queue <- importado no arquivo da árvore para que consigamos fazer uso da estrutura

import random
from binary_tree import BinarySearchTree

random.seed(77)

def random_tree(): # fazendo uma inserção, dinâmica, aleatória e retornando essa árvore modificada como resultado para uso

    values = random.sample(range(1, 1001), 42)
    tree = BinarySearchTree()

    for value in values:
        tree.insert(value)

    return tree

def example_tree(): # ESSA FUNÇÃO ESTÁ AQUI APENAS PARA FAZER UMA EXIBIÇÃO EM NÍVEL DOS ITENS PRESENTES NA ÁRVORE EXEMPLAR DO ARQUIVO
                    # tree_concepts.txt - na aba "percursos em árvores - percurso em nível"

    values = [61, 89, 66, 43, 51, 16, 55, 11, 79, 77, 82, 32] # <- são os mesmo valores presentes lá, para vermos se os números estão
    tree = BinarySearchTree()                                # sendo vistos nível a nível com a mesma estrutura do exemplo

    for value in values:
        tree.insert(value)

    return tree

binary_search_tree = example_tree()
binary_search_tree.levelorder_search()

# usando das estruturas já criadas para exibir e exemplificar o maior e o menor valor 
print()
print('-'*10, 'exibindo máximo e minimo', '-'*10)
print()
print('Máximo:', binary_search_tree.search_max()) # <- se rodarmos do jeito que está sem parâmetrar nada, teremos como raiz o primeiro nó 
print('Mínimo:', binary_search_tree.search_min()) # <- se parâmetrar um valor X, o nó da vez vai ser assumido por esse valor, 
                                                     # e a raiz passará a ser o valor parâmetrado, sendo assim, o processo seguirá rodando 
                                                     # a partir daquele nó.
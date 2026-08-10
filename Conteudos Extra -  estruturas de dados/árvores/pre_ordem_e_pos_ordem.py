# Usando a recursão para fazer uma exibição dinâmica dos elementos presentes nos nós

from binary_tree import BinaryTree, Node

def posorder_tree():
    tree = BinaryTree()

    n1 = Node('P')
    n2 = Node('R')
    n3 = Node('O')
    n4 = Node('G')
    n5 = Node('R')
    n6 = Node('A')
    n7 = Node('M')
    n8 = Node('A')
    n9 = Node('R')
    n0 = Node('✅')

    n0.left = n6
    n0.right = n9
    n6.left = n1
    n6.right = n5
    n5.left = n2
    n5.right = n4
    n4.right = n3
    n9.left = n8
    n8.right = n7

    tree.root = n0
    return tree

def preorder_tree():
    tree = BinaryTree()
    
    n1 = Node('P')
    n2 = Node('R')
    n3 = Node('O')
    n4 = Node('G')
    n5 = Node('R')
    n6 = Node('A')
    n7 = Node('M')
    n8 = Node('A')
    n9 = Node('R')
    n0 = Node('✅')

    n0.left = n6
    n0.right = n9
    n6.left = n1
    n6.right = n5
    n5.left = n2
    n5.right = n4
    n4.right = n3
    n9.left = n8
    n8.right = n7

    tree.root = n0
    return tree

if __name__ == '__main__':
    tree = posorder_tree()
    print('Percurso em pós ordem: ')
    print('-'*10)
    tree.posorder_search()
    print('-'*10)
    print(f'Altura: {tree.height()}')
    print('-'*10)
    tree = preorder_tree()
    print('Percurso em pós ordem: ')
    print('-'*10)
    tree.preorder_search()
    print('-'*10)
    print(f'Altura: {tree.height()}')
    print('-'*10)
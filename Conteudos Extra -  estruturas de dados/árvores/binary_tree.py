# Implementando uma árvore binária, esse arquivo será usado como base para todos os arquivos exemplo.py criados

from queue import Queue # <- importando estrutura de dados para uso no novo meétodo implementado "levelorder_search"

ROOT = 'root' # criando um modelo de constante para servir de ponto de partida na execução do programa para rodar saindo a partir da raiz
              # sem precisar passar um nó específico

class Node:

    def __init__(self, data):
        self.data = data
        self.left = None # <- Lembre-se que o modelo de árvore binária exige obrigatóriamente do dev a implementação de dois dados
        self.right = None # em seguimento de cascata

        return

    def __str__(self): # <- Serve para retornar uma string do dado fornecido 
        return str(self.data)
    
class BinaryTree: # <- Responsável pela parte inteligente da árvore, manipulando os métodos e tratando os dados passados na classe Node()

    def __init__(self, data=None, node=None):
        if node: # <- agora conseguimos construir uma sub-árvore a partir de um nó
            self.root = node
        elif data: # <- modificação implementada para poder usar o BinaryTree sem precisar passar algum dado como parâmetro
            node = Node(data) # <- objeto criado para inserir um dado a ser trata-do como a raiz da árvore
            self.root = node
        else:
            self.root = None

        return

    # método que faz o percurso em ordem simétrica
    def simetric_search(self, node=None):

        if node is None: # <- esse bloco confere se o nó está vazio, caso sim, percorra a partir da raiz
            node = self.root

        if node.left:
            print('(', end='') # <- exibindo parenteses de abertura antes de terminar a sub-árvore da esquerda
            self.simetric_search(node.left) # <- exibindo os itens sempre partindo da esquerda caso exista item na posição

        print(node, end='') # <- exibindo o item central com o "end='" para exibir tudo na mesma linha

        if node.right:
            self.simetric_search(node.right) # exibindo o próximo item, direita
            print(')', end='') # <- exibindo parenteses de abertura antes de terminar a sub-árvore da esquerda
        return

    def posorder_search(self, node=None): # <- iniciando o valor do parâmetro para conseguir trabalhar sem inserir valores

        if node is None:
            node = self.root # <- se o nó estiver vazio, o nó passsa a ser a raiz

        if node.left:
            self.posorder_search(node.left) # conferindo primeiro a esquerda

        if node.right:
            self.posorder_search(node.right) # conferindo depois a direita
 
        print(node) # e por fim, exibindo a raiz, que no caso seria o nó da vez a ser exibido

    def inorder_search(self, node=None): # <- método criado para fazer a exibição dos nós de uma árvore de forma crescente/ordenada

        if node is None: # ao invés de visitar a raiz no final igual o pós ordem, visitamos no meio da execução
            node = self.root

        if node.left:
            self.inorder_search(node.left)

        print(node, end=' ')

        if node.right:
            self.inorder_search(node.right)

    def levelorder_search(self, node=ROOT): # <- fazendo essa modificação, podemos usar o valor None no meétodo com algum significado que faça
                                            # que faça sentido na execução
        if node == ROOT:                  
            node = self.root # <- se o nó da vez for igual ao valor 'root', esse nó passa a ser a raiz da árvore

        queue = Queue()
        queue.push(node)

        while len(queue): # enquanto o tamanho da fila for maior que zero

            node = queue.pop()
            # na sequência, colocamos na fila os filhos desse nó armazenado antes de prosseguir com o resto da estrutura

            if node.left: # conferindo se os nós que estão a esqueda ou direita são diferentes de None
                queue.push(node.left)
            if node.right:
                queue.push(node.right)

            print(node, end=' ') # exibindo o nó da vez armazenado

    def preorder_search(self, node=ROOT): # não há segredo na compreensão de um percurso pré ordem, basta seguir a mesma ciência por trás do
                                          # pós ordem, com um diferencial que iremos sempre partir da raiz ao invès de deixar a raiz por último
        if node == ROOT: 
            node = self.root

        print(node) # exibe o nó da vez, que no momento é a RAIZ

        if node.left: # parte para a sub-árvore da esquerda
            self.preorder_search(node.left)

        if node.right: # parte para a sub-árvore da direita depois que todos os filhos da esquerda sumiram
            self.preorder_search(node.right)

    def height(self, node=None): # replicando o método acima aqui abaixo para calcular a altura de determinado lado de a árvore 

        if node is None:
            node = self.root 

        height_left = 0 # { valores iniciam com zero pois nas condicionais abaixo conferimos SE o valor do nó possui elemento
        height_right = 0 # } caso possua fazemos o cálculo, se não o valor se mantém em zero.

        if node.left:
            height_left = self.height(node.left) 

        if node.right:
            height_right = self.height(node.right) 

        # abaixo está a lógica do cálculo responsável pela altura do bloco
        if height_right > height_left:
            return height_right + 1
        else:
            return height_left + 1
    
class BinarySearchTree(BinaryTree):

    def insert(self, value):

        parent = None # <- variavel criada para conferência de tamanho do valor, por ex. testamos se x é maior y, caso seja jogamos x a direita
                        # caso não seja, irá ser alocado a esquerda.
        x = self.root

        while(x): # <- enquanto esse valor parâmetrado for diferente do vazio

            parent = x # <- vamos definir o parente pelo valor da vez na raiz 

            if value < x.data: # <- e em seguida vamos avançar esse valor do parente para alguma direção
                x = x.left
            else:
                x = x.right

        if parent is None: # <- isso aqui cria um nó com o valor parâmetrado para se tornar a raiz da árvore somente se CASO a raiz esteja vazia
            self.root = Node(value)
        elif value < parent.data:
            parent.left = Node(value)
        else:
            parent.right = Node(value)

    def search(self, value, node=0): # iniciando node com zero para sabermos que nenhum valor foi passado ao nó da vez

        if node == 0:
            node = self.root # <- se nada foi passado, a raiz passa a ser o valor do nó

        if node is None or node.data == value: # <- se node for vazio ou node for igual ao valor que estamos procurando na árvore binária
            return BinarySearchTree(node) # <- não faz sentido retornar o nó em si pois isso seria válido apenas se estivessimos trabalhando com
        # listas, já que não é o caso, podemos retornar uma sub-árvore, uma árvore que está iniciando A PARTIR daquele específico nó, para
        # não tornar a estrutura obsoleta. Porém para seguir com essa ideia de retorno da sub-árvore precisamos parâmetrar 'node no __init__ da
        # classe BinaryTree.

        if value < node.data: # <- nesse outro caso conferimos se o valor é menor que o node da vez
            return self.search(value, node.left) # <- descendo pela esquerda pois o valor é menor que o nó da vez
        else:
            return self.search(value, node.right) # operação inversa

    def search_min(self, node=ROOT): # <- definindo o valor de busca padrão a partir da raiz

        if node == ROOT:
            node = self.root

        while node.left: # enquanto existir nó a esquerda, siga descendo até chegar no útimo nó, esse será o menor valor
            node = node.left
        return node.data # retornando o último nó

    def search_max(self, node=ROOT):
        
        if node == ROOT:
            node = self.root

        while node.right: # enquanto existir nó a direita, siga descendo até chegar no útimo nó, esse será o maior valor
            node = node.right
        return node.data

    def remove(self, value, node=ROOT): # removendo o valor que queremos remover e o nó, caso não passarmos nada, será a raiz

        if node == ROOT:
            node = self.root

        if node is None:
            return node

        if value < node.data: # o valor que queremos remover for menor do que o nó da vez
                              # descemos pela esquerda
            # pós isso vamos substituir a sub-árvore a esquerda do nó pelo que a função irá nos retornar 
            # tentando remover esse mesmo valor do nó que está a esquerda, conferindo valor por valor até encontrar
            # o nó que desejamos remover
            node.left = self.remove(value, node.left)

            # seguir a mesma lógica acima, porém a direita
        elif value > node.data:
            node.right = self.remove(value, node.right)
        else: # quer dizer que encontramos o nó, pois o valor parâmetrado é igual
            # if node.left is None and node.right is None: # conferência de folha, caso não tenha filhos quer dizer que o mesmo é uma folha!
            #     return None # retornamos None para dizer que aquele cara foi removido e que ele agora equivale ao VAZIO.
            
            if node.left is None: # <- caso o filho da esquerda do nó removido seja vazio
                return node.right # <- ligamos a sub-árvore a direita ao nó que antecedia o nó removido
            # mesma lógica da condicional acima, alterando apenas o lado da sub-árvore
            elif node.right is None:
                return node.left
            else: # caso tenha filhos nos dois nós abaixo, teremos que calcular o substituto

                substitute = self.search_min(node.right) # <- substituto é o sucessor do valor a ser removido
                node.data = substitute # <- ao invés de trocar a posição dos nós, trocamos o valor
                node.right = self.remove(substitute, node.right) # <- depois, remove o substituto da subárvore à direita

            return node

        return
# testando as primeira funcionalidade da árvore binária
def main():
    # tree = BinaryTree(4) # <- Definindo a raiz da árvore
    # tree.root.left = Node(11) # <- Valor da esquerda
    # tree.root.right = Node(9) # <- Valor da direita

    # print(tree.root)
    # print(tree.root.left)
    # print(tree.root.right)

    tree = BinaryTree()
    n1 = Node('7')
    n2 = Node('+')
    n3 = Node('*')
    n4 = Node('8')
    n5 = Node('-')
    n6 = Node('/')
    n7 = Node('25')
    n8 = Node('3')
    n9 = Node('9')

    n6.left = n7
    n6.right = n8
    n5.left = n6
    n5.right = n9
    n3.left = n4
    n3.right = n5
    n2.left = n1
    n2.right = n3

    tree.root = n2
    tree.simetric_search()
    expressão = (7+(8*((25/3)-9)))
    print(f' = {expressão:.2f}') # <- valores ilusórios para fins didáticos

    return

if __name__ == '__main__':
    main()
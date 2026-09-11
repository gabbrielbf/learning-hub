from abc import ABC, abstractmethod

# Sistema de formatação DOCS
class ModeloDocs(ABC):
    def __init__(self, titulo='', autor='', data=''):
        self.titulo = titulo
        self.autor = autor
        self.data = data
    
    @abstractmethod
    def exibir_conteudo(self):
        pass

class Curriculo(ModeloDocs):
    def exibir_conteudo(self):
        return f'Titulo: {self.titulo} | Autor: {self.autor} | Data: {self.data}'
    
class WordDocs(ModeloDocs):
    def exibir_conteudo(self):
        return f'Titulo: {self.titulo} | Autor: {self.autor} | Data: {self.data}'

meu_curriculo = Curriculo('Meu curriculo', 'Desempregado', '18/06')
doc_word = WordDocs('Documento WORD', 'Microsoft', '19/05')
print()
print(meu_curriculo.exibir_conteudo())
print(doc_word.exibir_conteudo())

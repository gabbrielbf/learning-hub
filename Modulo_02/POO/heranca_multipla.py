class Animal:
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        pass


class Mamifero(Animal):
    def amamentar(self):
        return f'{self.nome}: está amamentando'


class Ave(Animal):
    def voar(self):
        return f'{self.nome}: está voando'


class Morcego(Mamifero, Ave):
    def emitir_som(self):
        return 'Morcegos emitem sons ultrassônicos'
    

morcego = Morcego(nome='Batman')

# Acessando métodos da classe base 'Animal
print('Nome do morcego: ', morcego.nome)
print('Som do morcego:', morcego.emitir_som())

print()
# Acessando métodos das classes 'Mamifero' e 'Ave'
print('Morcego amamentando: ', morcego.amamentar())
print('Morcego voando: ', morcego.voar())

# O robô assistente

class Eletrodomestico:
    def __init__(self):
        pass
    
    def ligar_tomada(self):
        return f'Conectando na tomada...'

class Computador:
    def processar_dados(self):
        return f'Processando informações...'
    
class RoboAssistente(Eletrodomestico, Computador):
    def __init__(self, modelo=''):
        super().__init__()
        self.modelo = modelo

    def dizer_ola(self):
        return f'Olá, sou o modelo {self.modelo}, como posso ajudar?'
    
mensagem = RoboAssistente('Eletrolux')

print()
print(mensagem.ligar_tomada())
print(mensagem.processar_dados())
print(mensagem.dizer_ola())
print()
print("\nExemplo de abstração:")
from abc import ABC, abstractmethod

class Veiculo(ABC):

  @abstractmethod
  def ligar(self):
    pass

  @abstractmethod
  def desligar(self):
    pass


class Carro(Veiculo):
  def __init__(self) -> None:
    pass

  def ligar(self):
    # Ligacao do carro
    return "Carro ligado usando a chave"
  
  def desligar(self):
    return "Carro desligado usando a chave"

carro_amarelo = Carro()
print(carro_amarelo.ligar())
print(carro_amarelo.desligar())


class Microondas:
    def __init__(self):
        # Detalhes complexos internos que o usuário não precisa ver
        self._voltagem = 220
        self._magnetron_ligado = False

    def _ligar_componentes_internos(self):
        # Lógica complexa escondida
        print("Ativando magnetron... Girando o prato... Emitindo ondas...")
        self._magnetron_ligado = True

    # ---- ISSO AQUI É A ABSTRAÇÃO ----
    # O usuário só vê e usa essa função simples!
    def esquentar_comida(self):
        self._ligar_componentes_internos()
        print("Comida esquentada com sucesso! Bip! Bip!")


# Isso aqui é o PADRÃO do controle remoto (a Interface)
class ControlePadrao(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def mudar_canal(self):
        pass

# Agora, qualquer TV criada PRECISA seguir esse padrão
class TVSAMSUNG(ControlePadrao):
    def ligar(self):
        print("Ligando tela QLED... Exibindo logo Samsung.")

    def mudar_canal(self):
        print("Mudando canal via sistema Tizen.")

class TVLG(ControlePadrao):
    
    
    def ligar(self):
        print("Ligando tela OLED... Exibindo logo LG.")

    def mudar_canal(self):
        print("Mudando canal via sistema WebOS.")

""" É passado como obrigatoriedade que todas as subclasses herdeiras da classe usuário tenham
um nome, uma data de nascimento e um sexo e isso não para por aí... """
class Usuario(ABC):
   @abstractmethod
   def nome(self):
    pass
   
   @abstractmethod
   def idade(self):
    pass
   
   @abstractmethod
   def sexo(self):
    pass

# Ao ter o parâmetro 'Usuário passado' dentro da subclasse 'Aluno' estamos firmando um contrato que OBRIGA a classe aluno
# Implementar os métodos definidos dentro da classe Usuário. 
class Aluno(Usuario):
   def nome(self):
      return f'Aluno: Marcos'
   def idade(self):
      return f'Idade: 34'
   def sexo(self):
      return f'Sexo: Masculino'

from rich import inspect

aluno1 = Aluno()
inspect(aluno1)
print(aluno1.nome(), aluno1.idade(), aluno1.sexo())

class Professor(Usuario): # <- A classe professor nunca funcionará pois ela não está seguindo o padrão que a classe 'Aluno' seguiu.
   pass


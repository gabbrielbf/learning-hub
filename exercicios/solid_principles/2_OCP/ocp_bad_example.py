'''
OPEN CLOSED PRINCIPLE

Imagine que uma clínica veterinária tem seu sistema próprio para aprovação de exames. No primeiro momento, ela tem um método para
verificar exame de sangue. Em outro ela adiciona exame por raio-x. Notamos no código que, conforme a clínica adiciona exames,
deverão adicionar uma validação para o exame. O que aumentaria a complexidade do código e a manutenção do mesmo.

A solução deste caso pode ser feita com o princípio aberto-fechado (Open Closed Principle). 
Utilizando do conceito do OCP, crie uma interface e classes que implementam a mesma para que, caso a clínica necessite de um novo
tipo de exame, uma nova classe seja adicionada, implementando métodos de uma interface padrão para exames.

'''


from abc import ABC, abstractmethod

class Exame(ABC):
    def __init__(self, tipo):
        self.tipo = tipo

    @abstractmethod
    def aprovar(self):
        """ Método abstrato que deve ser implementado por 
        cada tipo de exame específico. """
        pass


class ExameSangue(Exame):
    def __init__(self):
        super().__init__("sangue")

    def aprovar(self):
        print("Verificando condições específicas do exame de sangue...")
        print("Exame sanguíneo aprovado!")


class ExameRaioX(Exame):
    def __init__(self):
        super().__init__("raio-x")

    def aprovar(self):
        print("Verificando condições específicas do raio-x...")
        print("Raio-X aprovado!")


class AprovaExame:
    def aprovar_solicitacao_exame(self, exame: Exame):
        exame.aprovar()


if __name__ == "__main__":
    aprovador = AprovaExame()

    exame_sangue = ExameSangue()
    exame_raio_x = ExameRaioX()

    aprovador.aprovar_solicitacao_exame(exame_sangue)
    print("-" * 30)
    aprovador.aprovar_solicitacao_exame(exame_raio_x)
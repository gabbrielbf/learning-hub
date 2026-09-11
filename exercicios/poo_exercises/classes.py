# Vou importar as classes daqui, para deixar o código organizado

from abc import ABC, abstractmethod
from rich.panel import Panel
from rich import print as rprint

# Classes dos poligonos
class Poligonos(ABC):
    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Quadrado(Poligonos):
    def __init__(self, lado):
        self.lado = lado 

    def perimetro(self):
        return self.lado * 4
    
    def area(self):
        return self.lado * self.lado


class Circulo(Poligonos):
    def __init__(self, raio):
        self.raio = raio
        self.pi = 3.14 

    def perimetro(self):
        return 2 * self.pi * self.raio
    
    def area(self):
        return self.pi * (self.raio * self.raio)

# Classes da cafeteria
class BebidaQuente(ABC):
    def preparar(self):
        print('\n--- Iniciando Preparo ---')
        print(f'1. Fervendo água para beber ({self.nome_bebida})!')
        return
    
    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        print('--- Bebida pronta ---\n')
        pass


class Cafe(BebidaQuente):
    def __init__(self, nome_bebida=''):
        self.nome_bebida = nome_bebida
        return
    
    def preparar(self):
        super().preparar()
        self.misturar()
        self.servir()
        return 

    def misturar(self):
        print(f'2. Passando água quente dentre o café em pó.')
        return super().misturar()
    
    def servir(self):
        print(f'3. Servindo em xícara de vidro')
        return super().servir()


class Cha(BebidaQuente):
    def __init__(self, nome_bebida=''):
        self.nome_bebida = nome_bebida
        return
    
    def preparar(self):
        super().preparar()
        self.misturar()
        self.servir()
        return 

    def misturar(self):
        print(f'2. Derramando água encima de sachê.')
        return super().misturar()
    
    def servir(self):
        print(f'3. Servindo em xícara de porcelana')
        return super().servir()


class LeiteQuente(BebidaQuente):
    def __init__(self, nome_bebida=''):
        self.nome_bebida = nome_bebida
        return
    
    def preparar(self):
        super().preparar()
        self.misturar()
        self.servir()
        return 

    def misturar(self):
        print(f'2. Misturando com colher de pau.')
        return super().misturar()

    def servir(self):
        print(f'3. Servindo em copo térmico.')
        return super().servir()
    
# Classes dos calculos de frete
class Transporte(ABC):
    def __init__(self, distancia):
        self.distancia = distancia
        return 

    @abstractmethod
    def calc_frete(self):
        pass

""" Perceba que nas classes a baixo não definiremos o '__init__' PRESENTE na classe 'Transporte', não que isso seja uma regra até porquê
se colocarmos os inits nas classes filhas abaixo o código funcionará da mesma maneira. Porém a falta de presença desse '__init__' nos ensina
uma coisa importante na execução do programa. O código começa a rodar; Ele verá que a classe moto tem um argumento (x) dentro do objeto instânciado mas 
quando ele entra no bloco da classe percebe que ela não possui um '__init__', sendo assim vai na classe mãe buscar esse '__init__' e lá o
encontrará. Caso não tivessemos '__init__' na classe mãe ele nos daria um erro. """

class Moto(Transporte):
    def calc_frete(self):
        self.fator = 0.5
        self.frete = (self.distancia * self.fator)
        return f'{self.frete:.2f}'

  
class Caminhao(Transporte):
    def calc_frete(self):
        self.fator = 1.2
        if self.distancia >= 50:
            self.frete = (self.distancia * self.fator)
            return f'{self.frete:.2f}'
        else:
            return f'Caminhões fazem corridas acima de 50Km '


class Drone(Transporte):
    def calc_frete(self):
        self.fator = 9.5
        if (self.distancia > 0 and 
            self.distancia <= 10):
            self.frete = (self.distancia * self.fator)
            return f'{self.frete:.2f}'
        else:
            return f'O drone não tem bateria para viagens acima de [{self.distancia}Km], o limite é 10. '
        
# Calcular salário de diferentes funcionários
class Funcionario(ABC):
    def __init__(self, nome):
        self.nome = nome 
        self.salario_min = 1612
        self.inss = 7.5
        return
    
    @abstractmethod
    def calc_salario(self):
        pass

    def analisar_salario(self):
        qtd_salarios = self.salario / self.salario_min
        return f"O salário de {self.nome} ({self.__class__.__name__}) é de\nR${self.salario:.2f} e corresponde a {qtd_salarios:.1f} salários mínimos."


class Pedreiro(Funcionario):
    def __init__(self, nome, val_hora, horas_trab):
        super().__init__(nome)
        self.val_hora = val_hora
        self.horas_trab = horas_trab
    
    def calc_salario(self):
        self.salario = (self.val_hora * self.horas_trab)
        return f'O valor do salário do pedreiro [{self.nome}] é: {self.salario:.2f}'
        

class Professor(Funcionario):
    def __init__(self, nome, sal_bruto):
        super().__init__(nome)
        self.sal_bruto = sal_bruto
    
    def calc_salario(self):
        self.sal_liq = self.sal_bruto - (self.sal_bruto * (self.inss / 100))
        self.salario = self.sal_liq
        return f'O valor do salário do professor [{self.nome}] é: {self.salario:.2f}'
        

class Relatorio:
    @staticmethod
    def exibir(funcionario):
        funcionario.calc_salario()
        texto = funcionario.analisar_salario()
        rprint(Panel(texto, title="Análise de Salário", border_style="white"))

# Exercicio 1 - Sistema simples de pagamento
class MetodoPagamento(ABC):
    
    @abstractmethod
    def processar_pagamento(self, valor):
        pass


class CartaoCredito(MetodoPagamento):
    def processar_pagamento(self, valor):
        self.valor = valor
        return f'Processando valor de: R${self.valor:.2f} no crédito.'


class Pix(MetodoPagamento):
    def processar_pagamento(self, valor):
        self.valor = valor
        return f'Processando valor de: R${self.valor:.2f} no PIX.'
    
# Exercicio 2 - Sistema simples de notificações
class Notificador(ABC):
    
    @abstractmethod
    def enviar_mensagem(mensagem):
        pass


class Email(Notificador):
    def __init__(self, endereco_email):
        self.endereco_email = endereco_email
        return

    def enviar_mensagem(self, mensagem):
        return f'Enviando E-mail para: [{self.endereco_email}] -> {mensagem}'
  

class SMS(Notificador):
    def __init__(self, numero_telefone):
        self.numero_telefone = numero_telefone
        return
    
    def enviar_mensagem(self, mensagem):
        return f'Enviando SMS para: [{self.numero_telefone}] -> {mensagem}'  

# Exercicio 3 - Sistema simples de relatórios
# Classes abstratas
class Relatorio(ABC):

    @abstractmethod
    def gerar_conteudo(dados):
        pass


class Exportador(ABC):

    @abstractmethod
    def exportar_conteúdo(conteudo):
        pass

# Classes concretas
class ExportarPDF(Exportador):
    def exportar_conteúdo(self, conteudo):
        PDF_exportado = f'Exportando para PDF: [{conteudo}]'
        return PDF_exportado


class ExportarTXT(Exportador):
    def exportar_conteúdo(self, conteudo):
        TXT_exportado = f'Exportando para TXT: [{conteudo}]'
        return TXT_exportado

# Classes Objetos
class RelatorioFinanceiro(Relatorio):
    
    def gerar_conteudo(self, dados):
        dados_financeiros = f'Tivemos R${dados:.2f} de lucro este mês!'
        return dados_financeiros


class RelatorioVendas(Relatorio):
    def gerar_conteudo(self, dados):
        dados_vendas = f'Tivemos {dados} vendas este mês!'
        return dados_vendas

# RPG Simples
import random
class Personagem(ABC):
    def __init__(self, nome, vida=100):
        self.nome = nome
        self.vida = vida
        self.golpes = ['Ataque giratório', 'Voadora', 'Porrada com bastão']
        self.golpes = random.choice(self.golpes)
        return

    def atacar(self, alvo, forca):
        self.alvo = alvo
        self.forca = random.randint(0, forca)
        dano = self.forca
        self.receber_dano(dano)
        return

    def receber_dano(self, dano):
        dano = self.forca
        print(f'O jogador {self.nome} atacou o {type(self.alvo).__name__} com {self.golpes} e causou {dano} pontos de dano!')
        return 

    @abstractmethod
    def curar(self):
        pass


class Guerreiro(Personagem):
    
    def curar(self):
        print(f'O Guerreiro {self.nome} se curou com ataduras e recuperou {random.randint(0, 100)} pontos de vida!')
        return


class Mago(Personagem):

    def curar(self):
        print(f'O Mago {self.nome} se curou com uma poção e recuperou {random.randint(0, 100)} pontos de vida!')
        return

# Sistema de conta bancária para treinar encapsulamento
class ContaBancaria:

    def __init__(self, id, nome, saldo=0):
        self.id = id # atrubuto público (+)
        self._titular = nome # atributo protegido (#)
        self.__saldo = saldo # atributo privado (-)
        print(f'Conta N° {self.id} criada com sucesso\nSaldo atual é de: R${self.__saldo:,.2f}\n')
    
    def __str__(self):
        # return f'A conta {self.id} de {self.titular} tem {self.saldo:,.2f} de saldo.'
        return f'Estado atual da conta: {self.__dict__}'
    
    def depositar(self, valor):
        valor = abs(valor)
        self.__saldo += valor
        print(f'Depósito de R${valor:,.2f} autorizado na conta {self.id}')
        return

    def sacar(self, valor):
        valor = abs(valor)
        if valor > self.__saldo:
            print(f'SAQUE de {valor} na conta {self.id} NEGADO! Saldo insuficiente: {self.__saldo}')
        else:
            self.__saldo -= valor
            print(f'Saque de R${valor:,.2f} autorizado na conta {self.id}')
        return

# Sistema de avaliacao para treinar acesso de dados em encapsulamento
class Avaliacao:
    def __init__(self, nome, disciplina, nota):
        self.nome = nome
        self.disciplina = disciplina
        self._nota = nota # <- Atributo protegido
        return
    
    # def get_nota(self): # <- Métodos getters (acessor de valor)
    #     return self._nota

    # def set_nota(self, valor): # <- Métodos setters (acessor de valor OU alterar valor)
    #     if 0 <= valor <= 10:
    #         self._nota = valor
    #     else:
    #         print('Nota inválida!')
    #     return
    
    # Trabalhando coma atributos válidaveis
    @property
    def nota(self):
        return self._nota
    
    @nota.setter
    def nota(self, valor):
        if 0 <= valor <= 10:
            self._nota = valor
        else:
            print('Nota inválida!')
        return


class Termostato:
    def __init__(self):
        self.__temperatura = 24.0
        return
    
    @property
    def temperatura(self):
        self.__temperatura
        return

    @temperatura.setter
    def temperatura(self, temperatura):
        temperaturas_aceitas = [16.0, 16.5, 17.0, 17.5, 18.0, 18.5, 19.0, 19.5, 20.0, 
                                20.5, 21.0, 21.5, 22.0, 22.5, 23.0, 23.5, 24.0, 24.5,
                                25.0, 25.5, 26.0, 26.5, 27.0, 27.5, 28.0, 28.5, 29.0,
                                29.5, 30.0]
        
        if (temperatura > temperaturas_aceitas[-1]):
            self.temperatura = temperaturas_aceitas[-1]
            raise ValueError (f'A temperatura [{temperatura}°] não é válida! Escolha um valor dentre: [{temperaturas_aceitas[0]}° e {temperaturas_aceitas[-1]}°]')
        
        elif (temperatura < temperaturas_aceitas[0]):
            self.temperatura = temperaturas_aceitas[0]
            raise ValueError (f'A temperatura [{temperatura}°] não é válida! Escolha um valor dentre: [{temperaturas_aceitas[0]}° e {temperaturas_aceitas[-1]}°]')
        
        elif (temperatura not in temperaturas_aceitas):
            raise ValueError (f'A temperatura [{temperatura}°] não é válida! Escolha um valor dentre: [{temperaturas_aceitas[0]}° e {temperaturas_aceitas[-1]}°]')
        
        else:
            self.__temperatura = float(temperatura)
    
    @temperatura.getter
    def ftemperatura(self):
        print(f'Temperatura atual do termometro: {self.__temperatura}°C')
        return 


class Diario:
    def __init__(self):
        self.__segredos = []
        self.__senha = 'MinhaSenha123'

    def anotar_algo(self, msg): # <- Método de adição aos segredos do diário
        self.__segredos.append(msg)
        return

    def ler_conteudo(self, senha='123456'): # <- Método getter, para obter o conteúdo através da senha
        if (senha == self.__senha):
            print()
            print('Diário liberado!')
            for indice in range(0, len(self.__segredos)):
                print(f'Segredo N°{indice + 1}: {self.__segredos[indice]}')
            print()
        raise PermissionError(f'A senha [{senha}] não é a senha do diário!\nTente novamente.')


class Retangulo:
    def __init__(self, base=0, altura=0):
        self._base = base
        self._altura = altura
        return

    @property
    def base(self):
        return self._base
    @property
    def altura(self):
        return self._altura
    @property
    def area(self):
        return self._base * self._altura
    @property
    def medidas(self):
        return f'Base = {self._base}\nAltura = {self._altura}\nÁrea = {self._area:.2f}'
    
    @base.setter
    def base(self, base):
        if base > 0:
            self._base = base
        else:
            raise ValueError('O valor digitado é negativo!')

    @altura.setter
    def altura(self, altura):
        if altura > 0:
            self._altura = altura
        else: 
            raise ValueError('O valor digitado é negativo!')
    
    @medidas.setter
    def medidas(self, valores):
        base, altura = valores
        if base > 0 and altura > 0:
            self._base = base
            self._altura = altura
            self._area = base * altura
        else: 
            raise ValueError('O valor digitado é negativo!')


class Pessoa(ABC):
    ano_atual = 2026
    def __init__(self, nome='', nascimento=0): 
        self._nome = nome
        self._nascimento = nascimento

    @property
    def nome(self):
        return self._nome

    @property
    def nascimento(self):
        return self._nascimento

    @property
    def idade(self):
        return Pessoa.ano_atual - self._nascimento   


class Aluno(Pessoa):
    def __init__(self, nome='', nascimento=0, curso='ADM'):
        super().__init__(nome, nascimento) 
        self._curso = curso
        self.lista_cursos = ['ADS', 'ENF', 'FIS', 'ADM']

    def add_curso(self, curso=''):
        curso_maiusc = curso.upper()
        if curso_maiusc not in self.lista_cursos:
            curso_maiusc = curso.upper()
            self.lista_cursos.append(curso_maiusc)
        else:
            raise Exception('[ERRO] Curso já listado!')
        
    @property
    def curso(self):
        return self._curso
    
    @curso.setter
    def curso(self, curso=''):
        curso_maiusc = curso.upper()
        if curso_maiusc in self.lista_cursos:
            self._curso = curso_maiusc
        else:
            raise Exception('[ERRO] Curso não listado.')

# Criando um mini sistema de Spotify
class Midia(ABC):
    def __init__(self, titulo, artista, duracao):
        self.titulo = titulo
        self.artista = artista
        self.duracao = duracao 
        return

    @property
    def artista(self):
        return self.__artista
    
    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def duracao(self):
        return self.__duracao
    
    @artista.setter
    def artista(self, nome=''):
        self.__artista = nome

    @titulo.setter
    def titulo(self, titulo=''):
        self.__titulo = titulo
    
    @duracao.setter
    def duracao(self, duracao):
        if duracao > 0:
            self.__duracao = duracao
        else:
            raise Exception('Não é possível colocar uma duração negativa!')

    @abstractmethod
    def exibir_detalhes(self):
        pass

    def dar_play(self):
        return f'Dando play na mídia do artista {self.artista}'


class Musica(Midia):
    def __init__(self, titulo, artista, duracao, album):
        super().__init__(titulo, artista, duracao)
        self.album = album
        return

    @property
    def album(self):
        return self.__album
    
    @album.setter
    def album(self, album):
        self.__album = album

    def dar_play(self):
        return f'Dando play na música do artista {self.artista} do album {self.album}'
    
    def exibir_detalhes(self):
        return f'O titulo atual é: {self.titulo}\nO artista padrão é: {self.artista}\nA duração em segundos: {self.duracao}s\nAlbum: {self.album}'


class Podcast(Midia):
    def __init__(self, titulo, artista, duracao, host):
        super().__init__(titulo, artista, duracao)
        self.host = host

    @property
    def host(self):
        return self.__host
    
    @host.setter
    def host(self, host):
        self.__host = host

    def dar_play(self):
        return f'Dando play no podcast do canal {self.host}'
    
    def exibir_detalhes(self):
        return  f'O titulo atual é: {self.titulo}\nO host de hoje é: {self.host}\nA duração em segundos: {self.duracao}s'


class Playlist:
    def __init__(self):
        self.__playlist = []

    @property
    def playlist(self):
        if not self.__playlist:
            raise Exception('A playlist está vazia!')
        else:
            print('Playlist atual:')
            for i in range(0, len(self.__playlist)):
                print(f'{i + 1} - Artista: {self.__playlist[i].artista} | Midia: {self.__playlist[i].titulo}')
    
    @playlist.setter
    def playlist(self, midia):
        if (isinstance(midia, Midia)):
            self.__playlist.append(midia)
        else:
            raise Exception('O item não está no Spotify.')
    
    @property
    def duracao_playlist(self):
        if not self.__playlist:
            raise Exception('A playlist está vazia!')
        else:
            segundos_totais = 0
            for midia in self.__playlist:
                segundos_totais += midia.duracao
            print(f'Tempo de duração da playlist em segundos: {segundos_totais}s')

    def dar_play_em_tudo(self):
        if not self.__playlist:
            raise Exception('A playlist está vazia!')
        else:
            for midia in self.__playlist:
                print(f'--- {midia.__class__.__name__} ---')
                print()
                print(midia.dar_play())
                print(midia.exibir_detalhes())
                print()

# Criando um protótipo de assinaturas em streaming
class PlanoGenerico(ABC):
    def __init__(self, nome_plano, valor_plano):
        self._nome_plano = nome_plano
        self._valor_plano = valor_plano
        return
    
    @abstractmethod
    def calcular_preco_assinatura(self):
        pass


class PlanoPadrao(PlanoGenerico):
    def __init__(self, nome_plano, valor_plano, lim_telas=2):
        super().__init__(nome_plano, valor_plano)
        self._lim_telas = lim_telas
        return
    
    def calcular_preco_assinatura(self):
        return self._valor_plano


class PlanoPremium(PlanoGenerico):
    def __init__(self, nome_plano, valor_plano, anual):
        super().__init__(nome_plano, valor_plano)
        self._qual_plano = anual
        return
    
    def calcular_preco_assinatura(self):
        if self._qual_plano == 'anual':
            return self._valor_plano * 0.90
        else:
            return self._valor_plano


class Usuario:
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.plano = plano

    @property
    def nome(self):
        if self.__nome == None:
            raise Exception('O campo está vazio!')
        else:
            return self.__nome
    
    @property
    def email(self):
        if self.__email == None:
            raise Exception('O campo está vazio!')
        else:
            return self.__email
        
    @property
    def plano(self):
        if self.__plano == None:
            raise Exception('O campo está vazio!')
        else:
            return self.__plano
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @email.setter
    def email(self, email):
        if '@' not in email:
            raise Exception(f'O email: {email} não possui @!')
        else:
            self.__email = email
        
    @plano.setter
    def plano(self, plano):
        self.__plano = plano
    
    
class Streaming:
    def __init__(self):
        self.__usuarios = []

    def exibir_erro(self):
        raise Exception('A lista de usuários está vazia!')
    
    @property
    def usuarios(self):
        if not self.__usuarios:
            self.exibir_erro()
        else:
            return self.__usuarios
        
    @property
    def fatura(self):
        if not self.__usuarios:
            self.exibir_erro()
        else:
            total = 0
            print("--- Relatório de Faturamento Mensal ---")
            for indice, cliente in enumerate(self.__usuarios, start=1):
                valor_pago = cliente.plano.calcular_preco_assinatura()
                total += valor_pago
                print(f'{indice} - Cliente: {cliente.nome} | Email: {cliente.email} | Plano: {cliente.plano._nome_plano} | Pago: R${valor_pago:.2f}')
            print("-" * 35)
            print(f"Faturamento Geral da StreamFlex: R${total:.2f}")
            print()

    @usuarios.setter
    def usuarios(self, novo_usuario):
        if isinstance(novo_usuario, Usuario):
            self.__usuarios.append(novo_usuario)
        else:
            raise Exception('O usuário não se encaixa nos requisitos!')


class Catraca(ABC):
    def __init__(self, posicao):
        self.__posicao = posicao
        return
    
    @property
    def posicao(self):
        print(f'Posição da vez: {self.__posicao}')
        return
    
    @posicao.setter
    def posicao(self, posicao):
        if posicao > 0 and posicao <= 3:
            self.__posicao = posicao
        else:
            raise Exception('A catraca selecionada é inválida.')
        
    @abstractmethod
    def abrir_catraca(self):
        pass


class Catracacentral(Catraca):
    def abrir_catraca(self):
        print('Abrindo catraca central.')
        return

# Calculadora com classes
import operator
class Calculadora:
    def __init__(self, num1, operacao, num2):
        self.num1 = num1
        self.operacao = operacao
        self.num2 = num2

        self.operadores = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv
        }
    
    def calcular(self):
        func = self.operadores.get(self.operacao)
        if func:
            if self.operacao == '/' and self.num2 == 0:
                return "Erro: Divisão por zero!"
            return func(self.num1, self.num2)
        else:
            return "Operador inválido."

# Sistema inteligente Smart Home
class Dispositivo(ABC):
    
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @abstractmethod
    def status(self):
        pass

import random
class Lampada(Dispositivo):
    def __init__(self):
        self.intensidade = random.randint(0, 100)
        return
    
    def ligar(self):
        self.status_atual = 'Ligada'
        return f'Ligando a lâmpada na intensidade {self.intensidade}'
    
    def desligar(self):
        self.status_atual = 'Desligada'
        return f'Lâmpada desligada.'
    
    def status(self):
        if self.status_atual == 'Desligada':
            return f'A Lâmpada está {self.status_atual}.'
        elif self.status_atual == 'Ligada':
            return f'A Lâmpada está {self.status_atual} na intensidade {self.intensidade}.'
        else:
            raise Exception('Você precisa ligar ou desligar o dispositivo!')


class ArCondicionado(Dispositivo):
    def __init__(self):
        self.temperatura = random.randint(17, 30)
        return
    
    def ligar(self):
        self.status_atual = 'Ligado'
        return f'Ligando o Ar Condicionado na temperatura {self.temperatura}°'
    
    def desligar(self):
        self.status_atual = 'Desligado'
        return f'Ar condicionado desligado.'
    
    def status(self):
        if self.status_atual == 'Desligado':
            return f'O Ar Condicionado está {self.status_atual}.'
        elif self.status_atual == 'Ligado':
            return f'O Ar Condicinado está {self.status_atual} na intensidade {self.temperatura}.'
        else:
            raise Exception('Você precisa ligar ou desligar o dispositivo!')
    

class CameraSeguranca(Dispositivo):
    def __init__(self):
        self.gravacao = 'Modo gravação'
        return

    def ligar(self):
        self.status_atual = 'Ligada'
        return f'Ligando a Câmera no {self.gravacao}'
    
    def desligar(self):
        self.status_atual = 'Desligada'
        return f'Câmera desligada.'
    
    def status(self):
        if self.status_atual == 'Desligada':
            return f'A Câmera está {self.status_atual}.'
        elif self.status_atual == 'Ligada':
            return f'A Câmera está {self.status_atual} no modo {self.gravacao}.'
        else:
            raise Exception('Você precisa ligar ou desligar o dispositivo!')


class Casa:
    def __init__(self):
        self.__dispositivos = []
        return
    
    @property
    def dispositivo(self):
        if not self.__dispositivos:
            raise Exception('Lista vazia.')
        else:
            print()
            print('Desligando seus dispositivos:')
            for indice, dispositivo in enumerate(self.__dispositivos, start=1):
                print(f'{indice} - {dispositivo.desligar()}')
            print()

    @dispositivo.setter
    def dispositivo(self, dispositivo):
        if isinstance(dispositivo, (Lampada, ArCondicionado, CameraSeguranca)):
            self.__dispositivos.append(dispositivo)
        else:
            raise Exception('Dispositivo indisponível.')
        
    def ligar_todos(self):
        if not self.__dispositivos:
            raise Exception('Lista vazia.')
        else:
            print('Ligando todos os dispositivos:')
            for indice, dispositivo in enumerate(self.__dispositivos, start=1):
                print(f'{indice} - {dispositivo.ligar()}')
            print()

    def exibir_relatorio(self):
        if not self.__dispositivos:
            raise Exception('Lista vazia.')
        else:
            print('Relatório de dispositivos:')
            for indice, dispositivo in enumerate(self.__dispositivos, start=1):
                print(f'{indice} - {dispositivo.status()}')
            print()



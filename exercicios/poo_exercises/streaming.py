from classes import Streaming, Usuario, PlanoPadrao, PlanoPremium

# StreamFlex

""" O sistema precisa controlar diferentes tipos de planos, 
calcular faturamentos e gerenciar o acesso ao conteúdo. """

def main():
    plano_padrao = PlanoPadrao('Plano simples', 29.90)
    plano_premium = PlanoPremium('Plano PREMIUM', 49.90, 'anual')
    plano_premium2 = PlanoPremium('Plano PREMIUM', 49.90, 'mensal')

    cliente1 = Usuario('Marcos', 'marcao@gmail.com', plano_padrao)
    cliente2 = Usuario('Maria', 'mariazinha@gmail.com', plano_premium)
    cliente3 = Usuario('Jorge', 'Jorgin@gmail.com', plano_premium2)

    stream = Streaming()
    stream.usuarios = cliente1
    stream.usuarios = cliente2
    stream.usuarios = cliente3
    stream.fatura
    return

if __name__ == '__main__':
    main()
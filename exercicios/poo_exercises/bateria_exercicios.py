from classes import *

# Exercicio 1 - Sistema simples de pagamento  
p1 = CartaoCredito()
print()
print(p1.processar_pagamento(20))
p2 = Pix()
print(p2.processar_pagamento(20))
print()

# Exercicio 2 - Sistema simples de notificações

mensagem1 = 'Oi, eu estou aprendendo POO'
notificador1 = Email('python2026@gmail.com')

mensagem2 = 'POO é bastante complexo...'
notificador2 = SMS('92 00000-0000')

def disparar_notificacao(notificador, mensagem):
    print(notificador.enviar_mensagem(mensagem))
    print()
    return

disparar_notificacao(notificador1, mensagem1)
disparar_notificacao(notificador2, mensagem2)

# Exercicio 3 - Sistema simples de relatórios
financeiro1 = RelatorioFinanceiro()
vendas1 = RelatorioVendas()

exportar_pdf = ExportarPDF()
exportar_txt = ExportarTXT()

def chamar_relatorio(val1, val2):

    relat_finan = financeiro1.gerar_conteudo(val1).replace('.', ',')
    relat_vend = vendas1.gerar_conteudo(val2)

    print(exportar_pdf.exportar_conteúdo(relat_finan))
    print(exportar_txt.exportar_conteúdo(relat_vend))
    return 

chamar_relatorio(500, 50)
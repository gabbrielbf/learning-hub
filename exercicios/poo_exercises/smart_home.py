from classes import Casa, Lampada, ArCondicionado, CameraSeguranca

def main():
    lampada = Lampada()
    ar_condiciondo = ArCondicionado()
    camera_seguranca = CameraSeguranca()
    casa = Casa()

    casa.dispositivo = lampada
    casa.dispositivo = ar_condiciondo
    casa.dispositivo = camera_seguranca

    casa.dispositivo
    casa.ligar_todos()
    casa.exibir_relatorio()
    ar_condiciondo.desligar()
    casa.exibir_relatorio()
    lampada.desligar()
    casa.exibir_relatorio()
    lampada.ligar()
    camera_seguranca.desligar()
    casa.exibir_relatorio()

if __name__ == '__main__':
    main()
from classes import Musica, Podcast, Playlist
from rich import inspect

def main():
    # Cria e configura os objetos da música
    musica1 = Musica('Galinha pintadinha', 'João Paulo', 120, 'Vaqueiro apaixonado')
    musica2 = Musica('Seresta', 'Marcos VQJ', 195, 'Seresteiro da roça')
    musica3 = Musica('Rap do kratos', 'Tauz', 145, 'Rap geek')

    # Cria e configura os objetos do podcast
    podcast1 = Podcast('Live da madrugada', 'Mitico', 7500, 'Canal Podpah')
    podcast2 = Podcast('Live do almoço', 'igao', 5000, 'Canal Flow')
    podcast3 = Podcast('Live da manhã', 'Davy Jones', 8500, 'Canal Flow Games')

    # Cria a playlist e adiciona os objetos criados acima
    playlist1 = Playlist()
    playlist1.playlist = musica1
    playlist1.playlist = musica2
    playlist1.playlist = musica3
    playlist1.playlist = podcast1
    playlist1.playlist = podcast2
    playlist1.playlist = podcast3

    # Execução
    playlist1.playlist
    print()
    playlist1.duracao_playlist
    print()
    playlist1.dar_play_em_tudo()

if __name__ == '__main__':
    main()
class PlayList:
    def __init__(self, nome):
        self.nome = nome
        self.lista = []

    def adicionar_musica(self, musica):
        print(f'Musica adicionada a playlist {self.nome} | {musica}')
        return self.lista.append(musica)
    
    def tocar(self):
        if not self.lista:
            print(f'Nenhuma musica na playlist')
        else:
            for i, v in enumerate(self.lista):
                print(f'{i + 1}: Tocando: {v}')
                

usuario1 = PlayList('Gustavo')

usuario1.adicionar_musica('Teste')
usuario1.adicionar_musica('Teste342')
usuario1.tocar()
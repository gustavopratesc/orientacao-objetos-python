class ReprodutordeMidia:
    def tocar(self) -> None:
        pass

class Spotify(ReprodutordeMidia):
    def tocar(self):
        print(f'Tocando spotify agora!!')

class Youtube(ReprodutordeMidia):
    def tocar(self):
        print(f'Escutando musica e vendo video clipe no youtube !!')

class AppleMusic(ReprodutordeMidia):
    def tocar(self):
        print(f'Escutando musica no Iphone com Apple Music!')

class Pessoa:
    def __init__(self, nome, reprodutor: ReprodutordeMidia):
        self.nome = nome
        self.__reprodutor = reprodutor

    def tocar(self) -> None:
        print(f'{self.nome} está!!:')
        self.__reprodutor.tocar()


sp = Spotify()
yt = Youtube()
gu = Pessoa('Gustavo', sp)
joao = Pessoa('João', yt)

gu.tocar()
joao.tocar()

        
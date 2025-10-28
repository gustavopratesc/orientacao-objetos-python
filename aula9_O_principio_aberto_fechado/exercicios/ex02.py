class Artista:
    def __init__(self, tipo: str) -> None:
        self.tipo = tipo

    def apresentar_show(self) -> None:
        print(f'O {self.tipo} esta apresentando o show!')


class Circo:
    def apresentar(self, artista: Artista) -> None:
        print(f'O circo começa!!')
        artista.apresentar_show()
        print('A plateia aplaude!!!')

circo = Circo()

palhaco = Artista('Palhaço')

circo.apresentar(palhaco)

        
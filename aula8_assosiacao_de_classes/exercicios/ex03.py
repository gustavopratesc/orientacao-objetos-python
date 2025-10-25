class Computador:
    def ligar(self) -> None:
        print('Ligando o computador!')

    def desligar(self) -> None:
        print('Desligando o computador!')


class Usuario:
    def __init__(self, nome: str) -> None:
        self.nome = nome
    
    def usar(self, computador: Computador) -> None:
        computador.ligar()
        print(f'{self.nome} esta usando o pc!')

    def sair(self, computador: Computador) -> None:
        computador.desligar()
        print(f'{self.nome} desligou o computador!')


pc = Computador()

gustavo = Usuario('Gustavo')

gustavo.usar(pc)
gustavo.sair(pc)
        
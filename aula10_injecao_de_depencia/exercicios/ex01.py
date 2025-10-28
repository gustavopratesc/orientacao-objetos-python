class Computador:
    def __init__(self, navegador: str) -> None:
        self.navegador = navegador

    def abrir_navegador(self):
        print(f'Abrindo navegador: {self.navegador}')

    def abrir_editor(self):
        print(f'Abrindo editor...')

    
class Programador:
    def __init__(self, computador: Computador) -> None:
        self.__computador = computador
    
    def trabalhar(self) -> None:
        print(f'Ligando o computador')
        self.__computador.abrir_navegador()
        print(f'E tambem...')
        self.__computador.abrir_editor()

    


pcgamer = Computador('Pc, ryzen 5500u, placa 4060')

gustavo = Programador(pcgamer)

gustavo.trabalhar()
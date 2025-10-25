class Carro:
    def __init__(self, modelo: str) -> None:
        self.modelo = modelo
    
    def ligar(self) -> None:
        print(f'Ligando o {self.modelo}')

    def desligar(self) -> None:
        print(f'Desligando o {self.modelo}')
    

class Pessoa:
    def dirigir(self, carro: Carro) -> None:
        carro.ligar()
        print(f'Começando a dirigir o carro...')

    def estacionar(self, carro: Carro) -> None:
        carro.desligar()
        print(f'Estacionei o carro.')


gustavo = Pessoa()
carro1 = Carro('Corolla')

gustavo.dirigir(carro1)
gustavo.estacionar(carro1)
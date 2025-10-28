class Transporte:
    def mover(self):
        pass

class Carro(Transporte):
    def mover(self):
        print(f'Digirindo de carro ate o destino!')

class Bicicleta(Transporte):
    def mover(self):
        print(f'Pedalando ate o destino!')

class Patinete(Transporte):
    def mover(self):
        print(f'Patinando ate o destino!')

class Pessoa:
    def __init__(self, nome, transporte: Transporte):
        self.nome = nome
        self.__transporte = transporte

    def ir_trabalhar(self):
        self.__transporte.mover()
        print(f'{self.nome} está indo trabalhar!')


carro = Carro()
bike = Bicicleta()
patinete = Patinete()
gustavo = Pessoa('Gustavo', carro)
joao = Pessoa('João', bike)
sergio = Pessoa('Sergio', patinete)
gustavo.ir_trabalhar()
print()
joao.ir_trabalhar()
print()
sergio.ir_trabalhar()
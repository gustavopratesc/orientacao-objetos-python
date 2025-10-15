class Carro:
    def __init__(self, marca, modelo, cor, motor):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.motor = motor
        

    def caracteristicas(self):
        print(f'A marca do carro {self.marca}')
        print(f'O carro possui uma cor {self.cor}')
        print(f'E o motor de {self.motor} potência')

    
    def ligar(self):
        print(f'O carro {self.modelo} esta ligando!')


marca = input('Insira a marca do carro: ').strip().title()
modelo = input('Insira o modelo do carro: ').strip()
cor = str(input('Insira a cor: ')).strip().title()
if not cor.replace(' ', '').isalpha(): # trata o erro do espaço
    raise ValueError('ERRO: Insira apenas letras para cor!')

motor = float(input('Insira o motor do carro: '))

carro1 = Carro(marca, modelo, cor, motor)

carro1.ligar()

carro1.caracteristicas()

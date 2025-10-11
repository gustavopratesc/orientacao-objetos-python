class Carro:
    def __init__(self, modelo):
        self.modelo = modelo
        self.__ligado = False

    def ligar(self):
        self.__ligado = True
        self.__verificar_motor()

    def __verificar_motor(self):
        print(f'Motor funcionando normalmente!')

    def status(self):
        if self.__ligado:
            print('O carro esta ligado!!')
        else:
            print(f'O carro esta desligado!!')

carro1 = Carro('Corolla')

carro1.status()        
carro1.ligar()
carro1.status()
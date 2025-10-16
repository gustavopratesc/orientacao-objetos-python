class NivelBateria:
    def __init__(self):
        self.__nivel = 0

    @property
    def porcentagem_atual(self):
        return f'Bateria {self.__nivel}%'
    
    @porcentagem_atual.setter
    def definir_bateria(self, valor):
        if 0 <= valor <= 100:
            self.__nivel = valor
        else:
            print('ERRO: Insira um valor valido!')
    
celular = NivelBateria()

try:
    bateria = int(input('Insira a bateria: '))
except ValueError:
    print('ERRO: Insira valor inteiro!')

celular.definir_bateria = bateria

print(celular.porcentagem_atual)
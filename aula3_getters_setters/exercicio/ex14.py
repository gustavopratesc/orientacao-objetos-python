class Motor:
    def __init__(self):
        self.__velocidade = None

    @property
    def velocidade(self):
        return f'Velocidade atual {self.__velocidade}km/h'
    
    @velocidade.setter
    def definir_velocidade(self, km):
        if 0 <= km <= 200:
            self.__velocidade = km
        else:
            self.__velocidade = 200

m = Motor()

m.definir_velocidade = 180
print(m.velocidade)
m.definir_velocidade = 220
print(m.velocidade)
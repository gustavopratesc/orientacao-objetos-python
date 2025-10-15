class Carro:
    def __init__(self, modelo):
        self.modelo = modelo
        self.__velocidade = 0

    @property
    def velocidade_atual(self):
        return self.__velocidade
    
    @velocidade_atual.setter
    def velocidade_atual(self, nova_velocidade):
        if nova_velocidade == 0:
            print(f'O {self.modelo} esta parado!')
            return
        
        if nova_velocidade > 200:
            self.__velocidade = 200
            print(f'Devido a velocidade muito alta limitamos o {self.modelo} para {self.__velocidade}Km/h')

    
    def acelerar(self, nova_velocidade):
        self.__velocidade += nova_velocidade
        print(f'Acelerou +{nova_velocidade}Km/h')


carro1 = Carro('Corolla')

print(f'Velocidade atual: {carro1.velocidade_atual}Km/h')
carro1.acelerar(0)
print(f'Velocidade atual: {carro1.velocidade_atual}Km/h')
carro1.velocidade_atual = 250


##

class Carro:
    def __init__(self, modelo):
        self.modelo = modelo
        self.__velocidade = 0

    @property
    def velocidade_atual(self):
        return self.__velocidade
    
    @velocidade_atual.setter
    def velocidade_atual(self, nova_velocidade):
        if nova_velocidade == 0:
            print(f'O {self.modelo} está parado!')
            self.__velocidade = 0
        elif nova_velocidade > 200:
            self.__velocidade = 200
            print(f'Devido à velocidade muito alta, limitamos o {self.modelo} para {self.__velocidade}Km/h')
        else:
            self.__velocidade = nova_velocidade
            print(f'O {self.modelo} agora está a {self.__velocidade}Km/h')

    def acelerar(self, nova_velocidade):
        self.velocidade_atual = self.__velocidade + nova_velocidade


carro1 = Carro('Corolla')

carro1.velocidade_atual = 0      # Setter -> parado
carro1.acelerar(50)              # Acelera via setter
carro1.acelerar(180)             # Limite 200
print(f'Velocidade final: {carro1.velocidade_atual}Km/h')  # Getter

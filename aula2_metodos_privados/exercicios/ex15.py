from random import uniform

class SensorTemperatura:
    def __init__(self):
        self.__temperatura_real = uniform(20, 40)


    def ler_temperatura(self):
        return self.__ajustar_valor()

    def __ajustar_valor(self):
        return f'{self.__temperatura_real:.2f} °c'

        

temperatura = SensorTemperatura()

print(temperatura.ler_temperatura())
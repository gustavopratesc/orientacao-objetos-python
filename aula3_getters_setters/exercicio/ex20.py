class Temperatura:
    def __init__(self):
        self.__celsius = None
    
    @property
    def mostrar_temperatura(self):
        if self.__celsius is None:
            return f'Nenhuma temperatura declarada ainda!'
        return f'Temperatura em celcius: {self.__celsius}°C'
    
    @mostrar_temperatura.setter
    def definir_temperatura(self, valor):
        self.__celsius = valor


tempo1 = Temperatura()

print(tempo1.mostrar_temperatura)
tempo1.definir_temperatura = 31
print(tempo1.mostrar_temperatura)

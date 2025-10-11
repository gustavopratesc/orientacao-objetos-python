class Termometro:
    def __init__(self, temperatura) -> None:
        self.__temperatura = temperatura # se for None vai cair o valor 25

    @property
    def temperatura(self) -> float:
        return f'{self.__temperatura:.2f}°c'
    
    @temperatura.setter
    def temperatura(self, nova_temperatura):
        if isinstance(nova_temperatura, (int, float)) and nova_temperatura >= -273.13:
            self.__temperatura = nova_temperatura
        else:
            print('ERRO: Valor abaixo do zero absoluto!')


t = Termometro(12)
t.temperatura = 25 # mudando 
print(t.temperatura)
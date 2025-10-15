class Temperatura:
    def __init__(self):
        self.__celsius = None

    @property
    def celsius(self):
        return f'{self.__celsius}°C'
    
    @celsius.setter
    def celsius(self, valor):
        if -273 <= valor <= 1000:
            self.__celsius = valor
        else:
            print('Temperatura fora do intervalo permitido!')


t = Temperatura()

t.celsius = 15

print('Temperatura definida:',t.celsius)
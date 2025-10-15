class Contador:
    def __init__(self):
        self.inicio = 1
        self.contador = 0
        self.fim = 10

    def contar(self):
        
        while self.inicio:
            self.contador += 1
            print(self.contador)
            if self.contador == self.fim:
                break


teste = Contador()

teste.contar()
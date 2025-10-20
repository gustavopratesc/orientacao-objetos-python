class Carro:
    rodas = 4
    def __init__(self, cor):
        self.cor = cor
    

carro1 = Carro('vermelho')
carro2 = Carro('amarelo')

Carro.rodas = 2

carro1.rodas = 4

print(carro1.cor, carro1.rodas)
print(carro2.cor, carro2.rodas)
        
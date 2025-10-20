class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def ligar(self) -> str:
        return f'O carro esta ligado!'
    
    def detalhes(self) -> str:
        return f'''
        Marca: {self.marca}
        Modelo: {self.modelo}
        Ano: {self.ano}
'''
    

carro1 = Carro('Toyota', 'Corolla', 2020)

print(carro1.ligar())
print(carro1.detalhes())
        
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def apresentar(self):
        print(f'Olá meu nome é {self.nome} e tenho {self.idade} anos')


pessoa1 = Pessoa('Gustavo', 21)

pessoa1.apresentar()
        


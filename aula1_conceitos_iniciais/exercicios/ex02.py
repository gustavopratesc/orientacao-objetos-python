class pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def saudar(self):
        print(f'Olá meu nome é {self.nome} e eu tenho {self.idade} anos!')
        if self.idade < 18:
            print('Sou menor de idade!')


pessoa1 = pessoa('Gustavo', 15)

pessoa1.saudar()
    
        
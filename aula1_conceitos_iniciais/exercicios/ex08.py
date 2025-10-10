class Interacao:
    def __init__(self, nome):
        self.nome = nome
    
    def cumprimentar(self, outra_pessoa):
        print(f'Olá {outra_pessoa.nome}! Eu sou {self.nome}')

# outra_pessoa.nome acessa o nome da instacia da pessoa!
pessoa1 = Interacao('Gustavo')
pessoa2 = Interacao('Ana')

pessoa1.cumprimentar(pessoa2)
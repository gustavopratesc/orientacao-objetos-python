class Pessoa:
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def apresentar(self) -> str:
        return f'Olá {self.nome}, você possui {self.idade} anos e atualmente sua profissão é {self.profissao}'
    

pessoa1 = Pessoa('Gustavo', 21, 'Estudante')

print(pessoa1.apresentar())
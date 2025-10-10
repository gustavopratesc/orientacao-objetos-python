class pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def comparar_idade(self, outra_pessoa):
        if self.idade > outra_pessoa.idade:
            print(f'{self.nome} é mais velh(a) que {outra_pessoa.nome}.')
        elif self.idade < outra_pessoa.idade:
            print(f'{outra_pessoa.idade} é mais velh(a) que {self.idade}')
        else:
            print(f'Os dois possuem a mesma idade')


pessoa1 = pessoa('Gustavo', 21)
pessoa2 = pessoa('Ana', 18)

pessoa1.comparar_idade(pessoa2)
        
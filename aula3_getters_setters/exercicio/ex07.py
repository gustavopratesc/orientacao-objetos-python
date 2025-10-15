class Pessoa:
    def __init__(self, nome):
        self.nome = nome
        self.__idade = None

    @property
    def idade(self):
        if self.__idade is None:
            return 'Idadade não estabelecida'
        return f'{self.nome} possui {self.__idade} anos'
    
    @idade.setter
    def idade(self, nova_idade):
        if not isinstance(nova_idade, int) or not (0 <= nova_idade <= 120):
            raise ValueError('Idade invalida! Deve ser um número entre 0 e 120')
        self.__idade = nova_idade


pessoa1 = Pessoa('Gustavo')

pessoa1.idade = 15 # setter
print(pessoa1.idade) # getter
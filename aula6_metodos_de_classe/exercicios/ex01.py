class Pessoa:
    total_pessoas = 0

    def __init__(self, nome):
        self.nome = nome
        Pessoa.total_pessoas += 1
        self.id = Pessoa.total_pessoas

    @classmethod
    def mostrar_total(cls):
        print(cls.total_pessoas)
    

pessoa1 = Pessoa('Gustavo')
pessoa2 = Pessoa('Ana')
pessoa3 = Pessoa('Jose')

pessoa1.mostrar_total()

print(pessoa1.id)
print(pessoa2.id)
print(pessoa3.id)
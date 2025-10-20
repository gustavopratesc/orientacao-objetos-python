class Pessoa:
    total_pessoas = 0
    def __init__(self, nome):
        self.nome = nome
        Pessoa.total_pessoas += 1

pessoa1 = Pessoa('Gustavo')
pessoa2 = Pessoa('Amanda')
pessoa3 = Pessoa('Thais')
pessoa4 = Pessoa('Jane')


print(f'Total pessoas criadas (pela classe): {Pessoa.total_pessoas}')
print(f'Total pessoas criadas (pelo objeto): {pessoa1.total_pessoas}')
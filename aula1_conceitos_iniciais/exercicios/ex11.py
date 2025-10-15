class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def exibir_info(self):
        print(f'O produto {self.nome} custa {self.preco}')


produto1 = Produto('Shampoo', 15.99)

produto1.exibir_info()
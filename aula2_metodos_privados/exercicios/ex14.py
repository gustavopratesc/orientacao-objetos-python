class Produto:
    def __init__(self):
        self.__preco = None

    @property
    def preco(self):
        if self.__preco is not None:
            return f'R${self.__preco:.2f}'
        else:
            return f'Nenhum valor dado ainda'
    @preco.setter
    def preco(self, valor):
        if valor > 0:
            self.__preco = valor
        else:
            print('ERRO: Não pode valor negativo!')


produto1 = Produto()

print(produto1.preco)

produto1.preco = 1500

print(produto1.preco)


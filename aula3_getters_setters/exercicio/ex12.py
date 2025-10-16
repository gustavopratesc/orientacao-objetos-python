class Produto:
    def __init__(self, nome, preco):
        self.__nome = nome
        self.__preco = preco

    @property
    def preco(self):
        return f'Nome: {self.__nome} | Preco: R${self.__preco}'
    
    @preco.setter
    def preco(self, valor):
        if valor > 0:
            self.__preco = valor
        else:
            raise ValueError('ERRO: Insira valores validos!')

p = Produto('Mouse', 150)
print(p.preco)
p.preco = -150
print(p.preco)
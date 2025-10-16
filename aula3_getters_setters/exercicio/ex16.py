class Estoque:
    def __init__(self):
        self.__quantidade = 0

    @property
    def estoque(self):
        if self.__quantidade == 0:
            return f'Estoque Zerado! Repor Produto.'
        else:
            return f'Estoque Atual: {self.__quantidade} unidades'
    
    @estoque.setter
    def definir_estoque(self, quantidade):
        if quantidade < 0:
            raise ValueError('Estoque Negativo!')
        else:
            self.__quantidade = quantidade

loja = Estoque()

print(loja.estoque)

loja.definir_estoque = 150

print(loja.estoque)
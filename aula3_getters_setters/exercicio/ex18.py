class ProdutoEstoque:
    def __init__(self, nome, quantidade):
        self.__nome = nome
        self.__quantidade = quantidade

    @property
    def estoque(self):
        if self.__quantidade == 0:
            return f'⚠️  Estoque zerado — reabastecer!'
        return f'{self.__nome} | Quantidade: {self.__quantidade}'
    
    @estoque.setter
    def definir_estoque(self, qtd):
        if qtd < 0:
            raise ValueError('ERRO: Valor inserido negativo!')
        else:
            self.__quantidade = qtd
        
p = ProdutoEstoque('Teclado', 0)

print(p.estoque)

p.definir_estoque = 15

print(p.estoque)
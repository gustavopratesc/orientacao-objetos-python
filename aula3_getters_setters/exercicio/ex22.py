class Pedido:
    def __init__(self):
        self.__quantidade = None

    @property
    def pedido(self):
        if self.__quantidade < 0:
            return f'ERRO: Quantidade menor que 0'
        return f'Quantidade: {self.__quantidade}'
    
    @pedido.setter
    def pedido(self, valor):
        if valor > 0:
            self.__quantidade = valor
        else:
            print('ERRO: Insira valores positivos!')

    def finalizar_pedido(self):
        if self.__quantidade is None:
            print('Nenhum pedido na lista!')
        else:
            print(f'Pedido confirmado com {self.pedido} itens')

    
pedido1 = Pedido()

pedido1.finalizar_pedido()
pedido1.pedido = 15
print(pedido1.pedido)
pedido1.finalizar_pedido()
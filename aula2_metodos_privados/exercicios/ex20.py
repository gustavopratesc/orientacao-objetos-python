class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente
        self.lista = []
        self.__valor_total = 0

    def adicionar_pedido(self, preco):
        if preco > 0:
            self.lista.append(preco)
            print(f'Preço adicionado a lista: {preco}')
        else:
            print('Valor invalido')

    def finalizar_pedido(self):
        print(f'Total: R${self.__calcular_total():.2f}')
        print(f'Pedido Finalizado com sucesso!')

    def __calcular_total(self):
        self.__valor_total = sum(self.lista)
        return self.__valor_total
        
cliente = Pedido('Gustavo')
cliente.adicionar_pedido(15)
cliente.adicionar_pedido(16)
cliente.finalizar_pedido()
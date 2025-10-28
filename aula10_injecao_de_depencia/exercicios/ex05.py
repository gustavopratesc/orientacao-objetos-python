class Pagamento:
    def processar(self, valor: float):
        self.valor = valor


class PixPagamento(Pagamento):
    def processar(self, valor):
        print(f'Pagamento via pix no valor de R${valor:.2f}')

class CartaoCreditoPagamento(Pagamento):
    def processar(self, valor):
        print(f'Pagamento via cartão de credito R${valor:.2f}')

class Loja:
    def __init__(self, nome, pagamento: Pagamento):
        self.nome = nome
        self.__pagamento = pagamento

    def vender(self, valor: float):
        print(f'Loja {self.nome}')
        self.__pagamento.processar(valor)
    

pix = PixPagamento()

americanas = Loja('Americanas', pix)

americanas.vender(1500)
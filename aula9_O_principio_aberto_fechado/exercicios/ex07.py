'''classe base'''
class Pagamento:
    def processar(self) -> None:
        pass

'''sub classes'''

class Pix(Pagamento):
    def processar(self) -> None:
        print('Pagamento feito pelo pix com sucesso!')

class CartaoCredito(Pagamento):
    def processar(self) -> None:
        print('Pagamento feito pelo cartão de credito!')

class Boleto(Pagamento):
    def processar(self) -> None:
        print('Boleto pago com sucesso! Valido em ate 3 dias uteis')

'''classe que não pode modificar'''

class Caixa:
    def finalizar(self, pagamento: Pagamento) -> None:
        pagamento.processar()

caixa = Caixa()

pix = Pix()
cc = CartaoCredito()
boleto = Boleto()

caixa.finalizar(pix)
caixa.finalizar(cc)
caixa.finalizar(boleto)
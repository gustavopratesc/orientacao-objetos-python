class Loja:
    taxa = 1.15
    def __init__(self, valor_produto: float) -> None:
        self.valor_produto_bruto = valor_produto

    
    def consultar_valor_produto(self):
        valor_do_produto = self.valor_produto_bruto * self.taxa
        print(f'Valor do produto: R${valor_do_produto:.2f}')

    
    @classmethod
    def editar_taxa_do_produto(cls, valor: float):
        cls.taxa = valor
        print(f'Taxa modificada para: {valor}')
        
loja_praia = Loja(30.50)
loja_shooping = Loja(10.39)
loja_rua = Loja(20.33)

loja_praia.consultar_valor_produto()
loja_shooping.consultar_valor_produto()
loja_rua.consultar_valor_produto()

loja_praia.editar_taxa_do_produto(1.35)
print('-- EDITEI A TAXA --')
loja_praia.consultar_valor_produto()
loja_shooping.consultar_valor_produto()
loja_rua.consultar_valor_produto()
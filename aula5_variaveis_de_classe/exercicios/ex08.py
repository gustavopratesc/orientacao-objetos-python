class Loja:
    desconto = 0.25
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    def preco_com_desconto(self):
        total = self.preco - (self.desconto * self.preco)
        print(f'Você recebeu um desconto seu preço ficou R${total}')

produto1 = Loja('Shampoo', 15)
produto2 = Loja('Notebook', 1500)
produto1.preco_com_desconto()
produto2.preco_com_desconto()
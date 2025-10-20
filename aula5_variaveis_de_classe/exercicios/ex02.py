class Produto:
    estoque_total = 0
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        Produto.estoque_total += 1
        print(f'{self.nome} adicionado ao estoque.')

    def remover(self):
        Produto.estoque_total -= 1
        print(f'Produto removido!')


p1 = Produto('Shampoo', 8)
p2 = Produto('Sabonete', 4)
p2.remover()
p3 = Produto('Condicionador', 7)
p4 = Produto('escova', 4)


print(f'Estoque total: {Produto.estoque_total}')
print(f'Estoque individual: {p1.estoque_total}')
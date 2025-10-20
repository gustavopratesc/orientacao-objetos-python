class Produto:
    quantidade_criada = 0
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        Produto.quantidade_criada += 1
        self.id = self.quantidade_criada
    
    @classmethod
    def mostrar_quantidade(cls):
        print(cls.quantidade_criada)

    def produto(self):
        print(f'''
        Nome: {self.nome}
        Preço: {self.preco}
        Id: {self.id}
''')

p1 = Produto('Shampoo', 9)
p2 = Produto('Sabão', 5)
p3 = Produto('Condicionador', 7)

Produto.mostrar_quantidade()

p1.produto()
p2.produto()
p3.produto()
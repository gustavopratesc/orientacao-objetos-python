class Produto:
    def __init__(self, nome, preco_custo, preco_venda):
        self.nome = nome
        self.__preco_custo = preco_custo
        self.preco_venda = preco_venda

    def mostrar_lucrp(self):
        return f'''
        Produto: {self.nome}
        Lucro: {self.__calcular_lucro()}
'''
    
    def __calcular_lucro(self):
        lucro = self.preco_venda - self.__preco_custo
        return lucro
    
produto1 = Produto('Shampoo', 14, 16)

print(produto1.mostrar_lucrp())
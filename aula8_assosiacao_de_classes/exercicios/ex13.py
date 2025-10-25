class Produtos:
    def __init__(self) -> None:
        self.lista_produtos = []

    def adicionar_produto(self, nome: str, preco: float) -> None:
        self.lista_produtos.append({'produto': nome, 'preco': preco})


    def remover_produto(self, nome: str) -> None:
        for p in self.lista_produtos:
            if p['produto'] == nome:
                self.lista_produtos.remove(nome)
                break
        else:
            print('ERRO: Produto não encontrado')

    def formatacao(self, produto: dict) -> str:
        return f'Produto: {produto['produto']} | Preço R${produto['preco']:.2f}'

    def total(self) -> float:
        return sum(p['preco'] for p in self.lista_produtos)
        

class CarrinhoDeCompras:
    def __init__(self, nome: str) -> None:
        self.nome = nome

    def mostrar_carrinho(self, produto: Produtos) -> None:
        print(f'-- Carrinho de {self.nome} --')
        print('Itens')
        for p in produto.lista_produtos:
            print(produto.formatacao(p))
        print(f'Total R${produto.total()}')
        print('----------------------------')

produtos = Produtos()
produtos.adicionar_produto('Mouse', 50)
produtos.adicionar_produto('Teclado', 120)

carrinho = CarrinhoDeCompras('Gustavo')
carrinho.mostrar_carrinho(produtos)

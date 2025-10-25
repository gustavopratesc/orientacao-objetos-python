class Item:
    def __init__(self) -> None:
        self.lista_itens = []

    def adicionar_pedido(self, produto: str, preco: float) -> None:
        self.lista_itens.append({'produto': produto, 'preco': preco})

    def formatacao(self, produto: str, preco: float) -> None:
        return f'Produto: {produto} | Preço: R${preco:.2f}'

class Pedido:
    def __init__(self, nome) -> None:
        self.nome = nome
    
    def calcular_total(self, item: Item) -> float:
        total = sum(i['preco'] for i in item.lista_itens)
        return total

    def mostrar_tudo(self, item: Item) -> None:
        print(f'-- Pedido: {self.nome} --')
        print('----- ITENS -----')
        for i in item.lista_itens:
            print(f'Produto: {i['produto']} | Preço: R${i['preco']:.2f}')
        print(f'----------')
        print(f'Total: R${self.calcular_total(item):.2f}')

itens_gustavo = Item()
itens_gustavo.adicionar_pedido('Shampoo', 7)
itens_gustavo.adicionar_pedido('Sabonete', 5)
itens_gustavo.adicionar_pedido('Condicionador', 12)

gu = Pedido('Gustavo')
gu.mostrar_tudo(itens_gustavo)

    
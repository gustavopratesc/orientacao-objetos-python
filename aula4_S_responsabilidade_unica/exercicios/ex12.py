class Pedido:
    __lista_itens = [] # usar o __init__ para não juntar com outros clientes

    # def __init__(self, nome, preco):
    #     self.__nome = nome
    #     self.__preco = preco

    
    def adicionar_pedido(self, nome: str, preco: float) -> str:
        if not nome or not preco:
            return f'ERRO: Insira o nome e o preco'
        else:
            self.__lista_itens.append((nome, preco))
            return f'Item {nome} adicionado a lista!'
        
    def finalizar_pedido(self):
        resultado = ''
        for i, produto in enumerate(self.__lista_itens):
            resultado += f'{i + 1}: Produto: {produto}\n'
        return f'{resultado}\nTotal R${self.__calcular_total():.2f}'

    def __calcular_total(self):
        soma = sum([preco for nome, preco in self.__lista_itens])
        return soma
    

cliente = Pedido()

print(cliente.adicionar_pedido('Shampoo', 15))
print(cliente.adicionar_pedido('Condicionador', 8))
print(cliente.adicionar_pedido('Sabonete', 5))

print(cliente.finalizar_pedido())
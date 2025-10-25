class Garcom:
    def __init__(self, nome) -> None:
        self.nome = nome

    def atende_cliente(self) -> None:
        print(f'Garçom {self.nome} atende cliente!')

    def leva_pedido_cozinheiro(self, cozinheiro: "Cozinheiro", cliente: "Cliente", pedido: str) -> None:
        print(f'Garçom {self.nome} levou o pedido da mesa {cliente.mesa} para o cozinheiro.')
        cozinheiro.preparar_pedido(cliente, pedido)


class Cliente:
    def __init__(self, mesa: int) -> None:
        self.mesa = mesa

    def chama_garcom(self, garcom: "Garcom") -> None:
        garcom.atende_cliente()
        
    def faz_pedido(self, garcom: "Garcom", cozinheiro: "Cozinheiro", pedido: str) -> None:
        print(f'Cliente da mesa {self.mesa} faz o pedido: {pedido}')
        garcom.leva_pedido_cozinheiro(cozinheiro, self, pedido)


class Cozinheiro:
    def preparar_pedido(self, cliente: "Cliente", pedido: str) -> None:
        print(f'Cozinheiro está preparando o pedido da mesa {cliente.mesa}: {pedido}')
        print(f'Pedido da mesa {cliente.mesa} está pronto!')


gustavo = Cliente(5)
pedro = Garcom('Pedro')
joana = Cozinheiro()

gustavo.chama_garcom(pedro)
gustavo.faz_pedido(pedro, joana, 'X-burguer duplo carne')

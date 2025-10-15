class SistemaPedidos:
    def __init__(self, pedido: str, *valores: int) -> None:
        self.pedido = pedido
        self.valores = valores

    def processar_pedido(self) -> None:
        if self.__validar_pedido():
            total = self.__calcular_total()
            self.__gerar_recibo(total)
        else:
            print('ERRO: Insira valores corretos')



    # 1 validação
    def __validar_pedido(self) -> bool:
        return isinstance(self.pedido, str) and all(isinstance(v, int) for v in self.valores)
    
    # 2 calculo

    def __calcular_total(self) -> bool:
        return sum(self.valores)
    
    # 3 geração recibo

    def __gerar_recibo(self, total: int) -> None:
        print(f'Pedido: {self.pedido} | Valor R${self.valores} | Total R${total}')

pedido1 = SistemaPedidos('Caneta', 12, 45, 84, 88, 100)
pedido1.processar_pedido()
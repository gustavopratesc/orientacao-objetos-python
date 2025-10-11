class Produto:
    def __init__(self, nome) -> None:
        self.nome = nome
        self.__preco = None
    
    @property
    def preco(self) -> float:
        return self.__preco
    
    @preco.setter
    def preco(self, valor) -> None:
        if isinstance(valor, (int, float)) and valor >= 0:
            self.__preco = valor
        else:
            print('ERRO: Insira valores validos')

produto1 = Produto('shampoo')

produto1.preco = 5

print(f'{produto1.nome} custa R${produto1.preco:.2f}')
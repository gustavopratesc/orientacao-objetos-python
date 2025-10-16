class CadastroProduto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def cadastrar(self):
        if self.__validar_produto(self.nome, self.preco):
            self.__registrar_produto(self.nome, self.preco)
        else:
            self.__erro_dados()
    #

    def __validar_produto(self, nome: str, preco) -> bool:
        return isinstance(nome, str) and isinstance(preco, (int, float)) and preco > 0
    
    def __registrar_produto(self, nome: str, preco) -> None:
        print(f'Produto: {nome} | Preço: R${preco} | Registrado com sucesso!')

    def __erro_dados(self):
        print('ERRO: Insira os campos corretamente!')

produto1 = CadastroProduto('Shampoo', 15)
produto2 = CadastroProduto('Sabonete', 5)

produto1.cadastrar()
produto2.cadastrar()
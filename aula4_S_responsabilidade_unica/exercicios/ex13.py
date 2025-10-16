class ProdutoEstoque:
    def __init__(self):
        self.__lista = []

    def cadastrar(self, nome: str, preco: float, quantidade: int):
        if self.__validar_dados(nome, preco, quantidade):
            self.__lista.append(nome)
            self.__lista.append(preco)
            self.__lista.append(quantidade)
            return f'Estoque cadastrado com sucesso!'

    @property
    def exibir_informacoes(self):
        return f'''Produto {self.__lista[0]} | Preço {self.__lista[1]} | Quantidade {self.__lista[2]} | Total: {self.__calcular_total(self.__lista)}'''

    def __validar_dados(self, nome: str, preco: float, quantidade: int) -> bool:
        return isinstance(nome, str) and isinstance(preco, (int, float)) and isinstance(quantidade, int)

    def __calcular_total(self):
        total = self.__lista[1] * self.__lista[2]
        return total
    

estoque1 = ProdutoEstoque()

print(estoque1.cadastrar('Celular', 1000, 5))

print(estoque1.exibir_informacoes())

##########

class ProdutoEstoque:
    def __init__(self):
        self.__lista = []

    def cadastrar(self, nome: str, preco: float, quantidade: int):
        if self.__validar_dados(nome, preco, quantidade):
            self.__lista.append({
                'nome': nome,
                'preco': preco,
                'quantidade': quantidade
            })
            return 'Produto cadastrado com sucesso!'
        else:
            return 'ERRO: Dados inválidos!'

    @property
    def exibir_informacoes(self):
        if not self.__lista:
            return 'Nenhum produto cadastrado ainda!'

        resultado = ''
        for i, produto in enumerate(self.__lista):
            total = self.__calcular_total(produto['preco'], produto['quantidade'])
            resultado += (
                f"{i + 1}. Produto: {produto['nome']} | "
                f"Preço: R${produto['preco']:.2f} | "
                f"Quantidade: {produto['quantidade']} | "
                f"Total: R${total:.2f}\n"
            )
        return resultado

    def __validar_dados(self, nome: str, preco: float, quantidade: int) -> bool:
        return (
            isinstance(nome, str) and nome.strip() != '' and
            isinstance(preco, (int, float)) and preco > 0 and
            isinstance(quantidade, int) and quantidade > 0
        )

    def __calcular_total(self, preco: float, quantidade: int) -> float:
        return preco * quantidade


# Teste
estoque = ProdutoEstoque()
print(estoque.cadastrar('Celular', 1000, 5))
print(estoque.cadastrar('Fone de Ouvido', 200, 10))
print()
print(estoque.exibir_informacoes)

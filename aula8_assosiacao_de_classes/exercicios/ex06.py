class Endereco:
    def __init__(self, rua: str, cidade: str, estado: str) -> None:
        self.rua = rua
        self.cidade = cidade
        self.estado = estado
        

    def endereco_formatado(self) -> str:
        return f'Rua:{self.rua}\nCidade:{self.cidade}\nEstado:{self.estado}'

class Cliente:
    def __init__(self, nome: str, cpf: str) -> None:
        self.nome = nome
        self.cpf = cpf
        self.enderecos = []

    def adicionar_endereco(self, endereco: Endereco):
        self.enderecos.append(endereco)

    def mostrar_dados(self) -> None:
        print(f'Nome: {self.nome}\nCPF: {self.cpf}')
        print(f'Endereços: ')
        for endereco in self.enderecos:
            print(endereco.endereco_formatado())
            print('-' * 30)


# Criando o cliente
gustavo = Cliente('Gustavo Prates Caetano', '777.777.777-77')

# Criando endereços
e1 = Endereco('Rua dos Palmares', 'Vitória da Conquista', 'Bahia')
e2 = Endereco('Rua Guanabara', 'Goiânia', 'Goiás')

# Associando endereços ao cliente
gustavo.adicionar_endereco(e1)
gustavo.adicionar_endereco(e2)

# Exibindo os dados do cliente e seus endereços
gustavo.mostrar_dados()


    

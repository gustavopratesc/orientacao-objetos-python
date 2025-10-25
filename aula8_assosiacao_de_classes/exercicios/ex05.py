class Pessoa:
    def __init__(self, nome: str, cpf: str, endereco: "Endereco") -> None:
        self.nome = nome
        self.__cpf = cpf
        self.endereco = endereco

    def exibir_dados(self) -> None:
        print(f'Nome: {self.nome}\nCPF: {self.__cpf}')
        self.endereco.endereco_formatado()

class Endereco:
    def __init__(self, rua: str, cidade: str, estado: str) -> None:
        self.rua = rua
        self.cidade = cidade
        self.estado = estado

    def endereco_formatado(self) -> None:
        print(f'Rua: {self.rua}\nCidade: {self.cidade}\nEstado: {self.estado}')
    

endereco_Gustavo = Endereco('Rua palmares', 'Vitoria da conquista', 'Bahia')
Gustavo = Pessoa('Gustavo', '777.777.777-77', endereco_Gustavo)

Gustavo.exibir_dados()
class CadastroCliente:
    def __init__(self, nome: str, senha: int) -> None:
        self.__nome = nome
        self.__senha = senha
    
    def cadastro(self) -> None:
        if self.__validar_dados(self.__nome, self.__senha):
            self.__salvar_dados(self.__nome, self.__senha)
            self.__enviar_email()

    
    # metodos separados e organizados

    def __salvar_dados(self, nome: str, senha: int) -> None:
        print(f'Usuario {nome} salvo no banco de dados')


    def __validar_dados(self, nome: str, senha: int) -> bool:
        return isinstance(nome, str) and isinstance(senha, int)
    
    def __enviar_email(self) -> None:
        print(f'Foi enviado um email para sua caixa de entrada {self.__nome}')

cliente = CadastroCliente('Gustavo', 1234)
cliente.cadastro()
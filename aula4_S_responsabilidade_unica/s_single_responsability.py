class SistemaCadastral:
    def cadastrar(self, nome: str, idade: int) -> None:
        if self.__validade_input(nome, idade): 
            self.__register_user(nome, idade)
        else:
            self.__erro_handle()

    # Responsabilidades separadas!

    def __validade_input(self, nome:str, idade:int) -> bool:
        return isinstance(nome, str) and isinstance(idade, int)
    
    def __register_user(self, nome: str, idade: int) -> None:
        print('Acessando banco de dados!') 
        print(f'Cadastrar usuario {nome}, idade {idade}')

    def __erro_handle(self) -> None:
        print('Dados invalidos!')


pessoa1 = SistemaCadastral()
pessoa1.cadastrar('Gustavo', 21)
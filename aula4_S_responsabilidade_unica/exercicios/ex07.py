class Autenticacao:
    def __init__(self, usuario, senha):
        self.__usuario = usuario
        self.__senha = senha

    
    def login(self):
        if self.__validar_usuario(self.__usuario) and self.__validar_senha(self.__senha):
            print('Login efetivado com sucesso!')
        else:
            self.__validacao_erro()


    
    #

    def __validar_usuario(self, usuario) -> bool:
        if not usuario and len(usuario) < 5:
            return False
        else:
            return True
    
    def __validar_senha(self, senha) -> bool:
        return isinstance(senha, str) and len(senha) >= 8
    
    def __validacao_erro(self):
        print(f'ERRO: Insira credenciais corretas!')


usuario1 = Autenticacao('Gustavo', '153213255')

usuario1.login()
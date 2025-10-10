class Usuario:
    def __init__(self, login, senha):
        self.login = login
        try:
            self.__senha = int(senha)
        except ValueError:
            print('ERRO: Insira uma senha com números inteiros!')
            self.__senha = None

    def __verificar_senha(self, senha_digitada):
        return senha_digitada == self.__senha
        
    def login_usuario(self, senha_digitada):
        if self.__senha is None:
            print(f'Usuario invalido: senha não configurada corretamente')
            return

        if self.__verificar_senha(senha_digitada):
            print('Sucesso. Login efetivado com sucesso')
        else:
            print('Erro! Senha incorreta')


usuario1 = Usuario('gustavo', 1234)
usuario1.login_usuario(1234)  # ✅ Login realizado com sucesso!
usuario1.login_usuario(9999)  # ❌ Senha incorreta.
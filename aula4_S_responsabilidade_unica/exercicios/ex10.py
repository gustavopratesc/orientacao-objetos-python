class LoginSistema:
    def __init__(self, email, senha):
        self.__email = email
        self.__senha = senha

    def autenticar(self):
        if self.__validar_email(self.__email) and self.__validar_senha(self.__senha):
            return self.__acesso_permitido()
        else:
            return self.__erro_login()

    def __validar_email(self, email: str) -> bool:
        return isinstance(email, str) and '@' in email and '.com' in email
    
    def __validar_senha(self, senha: str) -> bool:
        return isinstance(senha, str) and len(senha) >= 6
    
    def __acesso_permitido(self) -> str:
        return '''✅ Acesso permitido!!!
        Bem-vindo ao sistema!
        Seu acesso foi registrado com sucesso.
        '''

    def __erro_login(self) -> str:
        return '❌ ERRO: Insira credenciais corretas!'
        

usuario = LoginSistema('gustavo@gmail.com', '123456')
print(usuario.autenticar())

class SistemaLogin:
    def __init__(self, usuario, senha):
        self.__usuarios = {'usuario': usuario, 'senha': senha}

    def __validar_login(self, usuario, senha):
        return usuario == self.__usuarios['usuario'] and senha == self.__usuarios['senha']
    
    def acessar(self, usuario, senha):
        if self.__validar_login(usuario, senha):
            print('Bem-vindo!')
        else:
            print('Credenciais Invalidas!')


pessoa1 = SistemaLogin('gustavo', 8179815710)

pessoa1.acessar('gustavo', 8179815710)
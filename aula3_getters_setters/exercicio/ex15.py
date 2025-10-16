class Usuario:
    def __init__(self):
        self.__senha = None

    @property
    def senha(self):
        return 'Senha protegida'
    
    @senha.setter
    def senha(self, senha):
        if len(str(senha)) >= 8:
            self.__senha = senha
        else:
            raise ValueError('ERRO: Insira uma senha valida!')
        
u = Usuario()

u.senha = 'Python2025'

print(u.senha)
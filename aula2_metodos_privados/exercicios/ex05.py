class SistemaSeguranca:
    def __init__(self, usuario):
        self.usuario = usuario
        self.__nivel_acesso = 'Alto'

    def verificar_usuario(self, nivel):
        print(f'{self.usuario} você tem acesso {nivel} ')
        self.__autorizar_entrada(nivel)

    def __autorizar_entrada(self, nivel):
        if nivel == self.__nivel_acesso:
            print(f'Acesso permitido')
        else:
            print('Acesso Recusado!')



usuario1 = SistemaSeguranca('Gustavo')

usuario1.verificar_usuario('Baixo')


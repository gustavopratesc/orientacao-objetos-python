class Usuario:
    def registrar(self):
        self.__validar_dados()
        self.__salvar_usuario()
        self.__enviar_email()


    def __validar_dados(self):
        print('validando nome e email')

    def __salvar_usuario(self):
        print('Salvando usuario no banco de dados')

    def __enviar_email(self):
        print('Enviando email de boas vindas...')


teste = Usuario()

teste.registrar()
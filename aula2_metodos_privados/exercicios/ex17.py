class Login:
    def __init__(self, email, senha):
        self.email = email
        self.senha = senha

    def autenticar(self):
        if self.__verificar_email() and self.__verificar_senha():
            return f'Login realizado com Sucesso!'
        else:
            return f'Credenciais invalidas!'

    def __verificar_email(self):
        return '@' in self.email and '.com' in self.email
    
    def __verificar_senha(self):
        return len(str(self.senha)) >= 6
            

usuario = Login('gustavoprates.c@gmail.com', '4864651321')

print(usuario.autenticar())
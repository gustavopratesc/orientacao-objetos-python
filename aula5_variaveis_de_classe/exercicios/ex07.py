class Usuario:
    usuarios_online = 0
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha
        

    def login(self):
        Usuario.usuarios_online += 1
        print(f'Usuario logado com sucesso!')
        
    def logout(self):
        Usuario.usuarios_online -= 1
        print(f'Usuario deslogado!')

    def mostrar_total_on(self):
        print(f'Total online: {self.usuarios_online}')


p1 = Usuario('Gu', 8179)
p2 = Usuario('jja', 15546)
p3 = Usuario('Ana', 465462)
p4 = Usuario('Jose', 5465222)

print(Usuario.usuarios_online)
p1.mostrar_total_on()
p1.login()
p1.logout()
p2.login()
p3.login()
p1.mostrar_total_on()
class Usuario:
    nivel_acesso = 'Basico'
    def __init__(self, estado):
        self.estado = estado

    @classmethod
    def trocar_acesso(cls):
        cls.nivel_acesso = 'Administrador'


p1 = Usuario(True)
p2 = Usuario(True)
p3 = Usuario(True)

print(p1.nivel_acesso)
print(p2.nivel_acesso)
print(p3.nivel_acesso)
print('-- MUDANDO USUARIOS PARA NIVEL ADM! --')
Usuario.trocar_acesso()
print(p1.nivel_acesso)
print(p2.nivel_acesso)
print(p3.nivel_acesso)
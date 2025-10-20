class Jogo:
    modo = 'SinglePlayer'
    def __init__(self):
        self.teste = True

    @classmethod
    def mudanca_modo(cls):
        cls.modo = 'Multiplayer'


p1 = Jogo()
p2 = Jogo()
p3 = Jogo()
#
print(p1.modo)
print(p2.modo)
print(p3.modo)
print(f'Mudando de modo para Multiplayer usando Jogo.mudanca_modo()')
Jogo.mudanca_modo()
print(p1.modo)
print(p2.modo)
print(p3.modo)
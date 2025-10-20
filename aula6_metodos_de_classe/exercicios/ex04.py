class Configuracao:
    modo = 'claro'
    def __init__(self, nome):
        self.nome = nome
    
    @classmethod # muda basicamente a variavel da classe!
    def alterar_modo(cls, novo_modo):
        cls.modo = novo_modo
    
    def mostrar_modo(self):
        print(f'Modo atual: {self.modo}')


teste1 = Configuracao('Gustavo')
teste2 = Configuracao('oi')
print(teste1.modo)
teste1.alterar_modo('escuro')
print(teste1.modo)
print(teste2.modo)
print(Configuracao.modo)


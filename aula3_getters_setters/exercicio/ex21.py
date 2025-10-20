class Usuario:
    def __init__(self):
        self.__senha = None
    
    @property
    def senha(self):
        if self.__senha is None:
            return f'Nenhuma senha definida ainda!'
        return '*' * len(str(self.__senha))
    
    @senha.setter
    def senha(self, valor):
        if len(str(valor)) >= 6:
            self.__senha = valor
        else:
            print(f'ERRO: SENHA TEM QUE TER PELO MENOS 6 CARACTERES')


p = Usuario()

print(p.senha)
p.senha = 1461321
print(p.senha)

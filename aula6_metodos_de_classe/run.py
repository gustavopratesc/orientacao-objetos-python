class MinhaClasse:
    estatico = 'Ficar estatico'
    def __init__(self, estado):
        self.__estado = estado

    def print_variavel_de_classe(self):
        print(self.estatico)

    @classmethod # <-- vai modificar a variavel de classe quando for chamada, em toda a classe independente de ela onde estiver
    def alteracao_de_variavel_de_classe(cls): # <- tem que usar o cls
        cls.estatico = 'Mudei aqui!'


obj1 = MinhaClasse(True)
obj2 = MinhaClasse(True)
obj3 = MinhaClasse(True)
print(obj1.estatico) # veja que se estiver antes do metodo a variavel de classe não ira mudar!

obj1.alteracao_de_variavel_de_classe()

print(obj1.estatico)
obj1.print_variavel_de_classe()
print(obj2.estatico)
print(obj3.estatico)
print(MinhaClasse.estatico)
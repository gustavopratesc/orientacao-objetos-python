class MinhaClasse:

    estatico = "Variavel estatica"

    def __init__(self, estado):
        self.estado = estado


obj1 = MinhaClasse(True)
obj2 = MinhaClasse(True)

MinhaClasse.estatico = 'Programador' # <-- a Variavel vai mudar para todos os objetos se for declarada junto com a classe

# agora se for declarada em um objeto ela permanece o mesmo valor
obj1.estatico = 'Aqui fica o mesmo valor'

print(obj1.estatico)
print(obj2.estatico)
print(MinhaClasse.estatico)
class Funcionario:
    proximo_id = 0
    def __init__(self, nome):
        self.nome = nome
        Funcionario.proximo_id += 1
        self.id = Funcionario.proximo_id

    

f1 = Funcionario('Gustavo')
print(f1.id)
f2 = Funcionario('Jose')
print(f2.id)
        
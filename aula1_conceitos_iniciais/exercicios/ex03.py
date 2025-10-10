class aniversario:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def fazer_aniversario(self):
        nova_idade = self.idade + 1
        print(f'{self.nome} fez aniversário agora tem {nova_idade} anos!')


pessoa1 = aniversario('Gustavo', 21)

pessoa1.fazer_aniversario()


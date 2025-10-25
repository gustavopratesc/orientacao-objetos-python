class Professor:
    def __init__(self, nome: str) -> None:
        self.nome = nome

    def ensinar(self) -> None:
        print(f'O professor {self.nome} esta dando aula!')

    
class Aluno:
    def __init__(self, nome: str) -> None:
        self.nome = nome

    def assistir_aula(self, professor: Professor):
        professor.ensinar()
        print(f'O aluno {self.nome} esta assistindo a aula!')
        


p = Professor('Lhama')
a = Aluno('Gustavo')

a.assistir_aula(p)
class Aluno:
    total_alunos = 0
    def __init__(self, aluno, matricula):
        self.aluno = aluno
        self.matricula = matricula
        Aluno.total_alunos += 1

    def mostrar_total(self):
        return f'Total alunos matriculados: {Aluno.total_alunos}'
        


aluno1 = Aluno('Gustavo', 12345)
aluno2 = Aluno('Jose', 12345465)
aluno3 = Aluno('Juca', 12345645)
print(Aluno.total_alunos)
print(aluno1.mostrar_total())
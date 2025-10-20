class Aluno:
    def __init__(self, nome, curso, lista=None):
        self.nome = nome
        self.curso = curso
        if lista is None:
            lista = []
        self.lista = lista

    def media(self):
        media = sum(self.lista) / len(self.lista)
        return f'Curso: {self.curso} Media das notas do aluno: {self.nome} é: {media:.2f}'
    

aluno1 = Aluno('Gustavo', 'Sistemas de informação', [15, 16, 19])

print(aluno1.media())
        
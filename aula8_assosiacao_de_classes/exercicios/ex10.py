# Professor e Disciplina:
# O professor ministra uma ou mais disciplinas. Crie métodos para adicionar e listar as disciplinas ministradas.

class Disciplina:
    def __init__(self, nome, turno) -> None:
        self.nome = nome
        self.turno = turno

    def formatacao(self) -> str:
        return f'Disciplina: {self.nome} | Turno: {self.turno}'
    

class Professor:
    def __init__(self, nome) -> None:
        self.nome = nome
        self.disciplinas = []

    def adicionar_disciplina(self, disciplina: Disciplina) -> None:
        self.disciplinas.append(disciplina)

    def mostrar_dados(self) -> None:
        print(f'-- Professor: {self.nome} --')
        print('------ DISCIPLINAS ------')
        for d in self.disciplinas:
            print(d.formatacao())



gustavo = Professor('Gustavo')

d1 = Disciplina('Algoritimos', 'Vespertino')
d2 = Disciplina('Programação orientada a objetos', 'Noturno')

gustavo.adicionar_disciplina(d1)
gustavo.adicionar_disciplina(d2)

gustavo.mostrar_dados()

jose = Professor('Jose')

d1 = Disciplina('Matematica', 'Manhã')

jose.adicionar_disciplina(d1)

jose.mostrar_dados()

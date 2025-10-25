class Curso:
    def __init__(self, nome: str, periodo: str) -> None:
        self.nome = nome
        self.periodo = periodo
        

    def curso_formatado(self) -> str:
        return f'Curso: {self.nome} | Periodo: {self.periodo}'



class Aluno:
    def __init__(self, nome: str, matricula: int) -> None:
        self.nome = nome
        self.matricula = matricula
        self.cursos = []

    def adicionar_curso(self, curso: Curso):
        self.cursos.append(curso)

    def mostrar_dados(self) -> None:
        print(f'Nome: {self.nome}\nMatricula: {self.matricula}')
        print(f'\n-- Cursos --')
        for c in self.cursos:
            print(c.curso_formatado())
            print('-' * 50)


gustavo = Aluno('Gustavo', 12345678910)

bsi = Curso('Sistemas de informação', 'Noturno')
tca = Curso('Tecnico em Alimentos', 'Manhã')

gustavo.adicionar_curso(bsi)
gustavo.adicionar_curso(tca)

gustavo.mostrar_dados()
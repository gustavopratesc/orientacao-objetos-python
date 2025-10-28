class Professor:
    def ministrar_aula(self) -> None:
        pass

class ProfessorMatematica(Professor):
    def ministrar_aula(self) -> None:
        print('O professor de matematica esta dando aula: 2+2 = 4')

class ProfessorHistoria(Professor):
    def ministrar_aula(self) -> None:
        print('O prefessor de historia esta dando aula: Os primeiros humanos descobriram o fogo...')

class ProfessorInformatica(Professor):
    def ministrar_aula(self) -> None:
        print('O professor de informatica esta dando aula: Int = Inteiro, Float = flutuante')

class ProfessorIngles(Professor):
    def ministrar_aula(self) -> None:
        print('O professor de inglês esta dando aula: Hi, students')

class PlataformaOnline:
    def iniciar_aula(self, professor: Professor) -> None:
        professor.ministrar_aula()


plataforma = PlataformaOnline()

p_mat = ProfessorMatematica()
p_his = ProfessorHistoria()
p_inf = ProfessorInformatica()
p_ing = ProfessorIngles()
print('Aula esta começando...')
plataforma.iniciar_aula(p_mat)
plataforma.iniciar_aula(p_his)
plataforma.iniciar_aula(p_inf)
plataforma.iniciar_aula(p_ing)
        

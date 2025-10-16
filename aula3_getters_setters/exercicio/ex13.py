class Aluno:
    def __init__(self):
        self.__nota = None

    @property
    def nota(self):
        if self.__nota >= 7:
            return 'Aprovado'
        elif 5 <= self.__nota < 7:
            return 'Recuperação'
        else:
            return 'Reprovado'
        
    @nota.setter
    def nota(self, valor):
        if 0 <= valor <= 10:
            self.__nota = valor
        else:
            raise ValueError('ERRO: Insira notas entre 0 a 10')
        
a = Aluno()
a.nota = 3
print(a.nota)
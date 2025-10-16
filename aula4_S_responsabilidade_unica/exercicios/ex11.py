class CadastroAlunoAvancado:
    __alunos = []

    def __init__(self, nome, matricula):
        self.__nome = nome
        self.__matricula = matricula


    
    def matricula(self):
        if self.__validar_dados(self.__nome, self.__matricula):
            return self.__cadastro(self.__nome, self.__matricula)
        else:
            return self.__validar_erro()

    def listar_alunos(self):
        if not self.__alunos:
            return f'Nenhum aluno na lista ainda!'
        
        resultado = ''
        for i, aluno in enumerate(self.__alunos):
            resultado += f"{i + 1}: {aluno['aluno']} | Matricula {aluno['matricula']}\n"
        return resultado

    def __validar_dados(self, aluno: str, matricula: int):
        return isinstance(aluno, str) and isinstance(matricula, int)

    def __cadastro(self, aluno: str, matricula: int) -> str:
        self.__alunos.append({'aluno': aluno, 'matricula': matricula})
        return f'''
             Aluno: {aluno}
             Matricula: {matricula}
             Cadastrado com sucesso!!
 '''
    
    def __validar_erro(self) -> str:
        return 'ERRO: Insira dados validos!'
    

aluno1 = CadastroAlunoAvancado('Gustavo', 12345678910)
aluno2 = CadastroAlunoAvancado('Ana', 10987654321)

print(aluno1.matricula())
print(aluno2.matricula())

print(aluno1.listar_alunos())
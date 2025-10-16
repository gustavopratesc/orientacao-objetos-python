class CadastroAluno:
    def __init__(self, nome: str, matricula: int) -> None:
        self.nome = nome
        self.matricula = matricula

    def cadastrar(self):
        if self.__validar_matricula(self.nome, self.matricula):
            return self.__registrar_aluno(self.nome, self.matricula)
        else:
            self.__validar_dados()

    #

    def __validar_matricula(self, nome: str, matricula: int) -> bool:
        return isinstance(nome, str) and isinstance(matricula, int)
    
    def __registrar_aluno(self, nome: str, matricula: int) -> str:
        return f'Aluno {nome} | Matricula: {matricula} registrado no banco de dados!'
    
    def __validar_dados(self):
        raise ValueError('ERRO: Insira credenciais corretas!')
    
aluno = CadastroAluno('Gustavo', 150)

print(aluno.cadastrar())
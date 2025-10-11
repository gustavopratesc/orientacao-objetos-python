class Aluno:
    def __init__(self, nome) -> None:
        self.nome = nome
        self.__nota = None

    @property
    def situacao_aluno(self) -> float:
        if self.__nota >= 7:
            return f'{self.nome} vc foi Aprovado com nota {self.__nota}'
        else:
            return f'{self.nome} vc foi Reprovado com nota {self.__nota}'
        
    @situacao_aluno.setter
    def situacao_aluno(self, nota) -> None:
        if isinstance(nota, (int, float)) and 0 <= nota <= 10:
            self.__nota = nota
        else:
            print('ERRO: Insira um valor valido!')


a = Aluno('Gustavo')
a.situacao_aluno = 10
print(a.situacao_aluno)


# ou

@property
def nota(self):
    return self.__nota

@nota.setter
def nota(self, valor):
    if isinstance(valor, (int, float)) and 0 <= valor <= 10:
        self.__nota = valor
    else:
        print('ERRO: Insira um valor válido!')

@property
def situacao(self):
    if self.__nota is None:
        return "Nota não definida"
    return f"{self.nome} foi {'Aprovado' if self.__nota >= 7 else 'Reprovado'} com nota {self.__nota}" # operador ternario

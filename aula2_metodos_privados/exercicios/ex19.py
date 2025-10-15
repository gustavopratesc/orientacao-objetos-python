class Aluno:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.__nota = None

    def definir_nota(self, nota):
        if 0 <= nota <= 10:
            self.__nota = nota
        else:
            print('ERRO: Insira notas entre 0 e 10')

    def mostrar_informacoes(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        self.__avaliar_situacao()

    def __avaliar_situacao(self):
        if self.__nota == None:
            print('Nenhuma nota definida ainda!')
            return
        
        if self.__nota >= 7:
            print('Aprovado')
        else:
            print('Reprovado')


aluno1 = Aluno('Gustavo', 21)

aluno1.mostrar_informacoes()
aluno1.definir_nota(1)
aluno1.mostrar_informacoes()
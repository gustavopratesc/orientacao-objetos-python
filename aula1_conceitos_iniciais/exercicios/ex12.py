class Aluno:
    def __init__(self, nome, serie, nota):
        self.nome = nome
        self.serie = serie
        self.nota = nota

    def status(self):
        if self.nota >= 7:
            print(f'{self.nome} foi aprovado na {self.serie}° serie | Nota: {self.nota}')
        else:
            print(f'{self.nome} foi reprovado na {self.serie}° serie!! | Nota: {self.nota}')

nome = str(input('Insira seu nome: ')).strip().title()
if not nome:
    print('ERRO: Insira um nome')
else:
    try:
        nota = int(input('Insira sua nota: '))
    except ValueError:
        print('ERRO: Insira valores validos!')

    serie = int(input('Insira sua serie da escola: '))

aluno1 = Aluno(nome, serie, nota)

aluno1.status()


    
        
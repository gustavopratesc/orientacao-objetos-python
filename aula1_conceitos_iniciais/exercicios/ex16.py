class Aluno:
    def __init__(self, nome, lista_notas):
        self.nome = nome
        self.lista_notas = lista_notas

    
    def media(self):
        media = sum(self.lista_notas) / len(self.lista_notas)
        if media >= 7:
            return f'{self.nome} foi aprovado com média {media:.2f}'
        else:
            return f'{self.nome} foi reprovado com média {media:.2f}'

nome = str(input('Insira o nome do aluno: ')).strip().title()
if not nome.replace(' ', '').isalpha():
    raise ValueError('ERRO: Insira um nome!')

lista_notas = []

try:
    qtd_notas = int(input('Insira a quantidade de notas: '))
    for i in range(qtd_notas):
        nota = float(input(f'Insira a {i + 1}° nota: '))
        lista_notas.append(nota)
except ValueError:
    print('ERRO: Insira apenas números!')

aluno1 = Aluno(nome, lista_notas)

print(aluno1.media())
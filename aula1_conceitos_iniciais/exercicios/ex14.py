class Filme:
    def __init__(self, titulo, ano, genero):
        self.titulo = titulo
        self.ano = ano
        self.genero = genero

    
    def descricao(self):
        print(f'O filme {self.titulo} é um genero de {self.genero} lançado no ano de {self.ano}')



filme1 = Filme('Vingadores', 2012, 'Ação')

filme1.descricao()
        
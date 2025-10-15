class Filme:
    def __init__(self, titulo):
        self.titulo = titulo
        self.__avaliacao = None

    @property
    def avaliacao(self):
        if self.__avaliacao is None:
            return f'Nenhuma avaliação para o filme {self.titulo}'
        
        return f'Filme {self.titulo} ganhou {self.__avaliacao} estrelas'
    
    @avaliacao.setter
    def avaliacao(self, add_avaliacao):
        if not isinstance(add_avaliacao, int) or not (0 <= add_avaliacao <= 10):
            raise ValueError('ERRO: Insira números inteiros entre 0 a 10')
        self.__avaliacao = add_avaliacao
    
avaliador1 = Filme('Vingadores')

avaliador1.avaliacao = 5

print(avaliador1.avaliacao)


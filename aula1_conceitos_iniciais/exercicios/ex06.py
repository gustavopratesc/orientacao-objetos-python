class cadastro_automatico:
    
    todas_pessoas = []

    def __init__(self, nome, idade):
        self.nome = nome
        try:
            self.idade = int(idade)
        except ValueError:
            print('ERRO: Insira uma idade valida')
            self.idade = 0
        
        self.__class__.todas_pessoas.append(self)

    @classmethod
    def mostrar_todas(cls):
        if not cls.todas_pessoas:
            print(f'Nenhuma pessoa cadastrada')
        else:
            print(f'-- Pessoas cadastradas --')
            for i, pessoa in enumerate(cls.todas_pessoas, start=1):
                print(f'{i} - Nome: {pessoa.nome} - idade: {pessoa.idade} anos')

pessoa1 = cadastro_automatico('Gustavo', 25)
pessoa2 = cadastro_automatico('João', 24)
pessoa3 = cadastro_automatico('Maria', '35')

cadastro_automatico.mostrar_todas()
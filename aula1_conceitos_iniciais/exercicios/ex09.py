class mini_sistema_cadastro:
    pessoas = []

    def __init__(self, nome):
        self.nome = nome
    
    def cadastrar_nova_pessoa(self):
        mini_sistema_cadastro.pessoas.append(self.nome)
        print(f'Pessoa {self.nome} cadastrada')

    def listar_pessoas(self):
        if not mini_sistema_cadastro.pessoas:
            print('Nenhuma pessoa na lista atual')
        else:
            print(f'-- Pessoas cadastradas --')
            for i, pessoa in enumerate(self.pessoas, start=1):
                print(f'{i}: {pessoa}')

    def sair_programa(self):
        print('Saindo do programa...')


pessoa1 = mini_sistema_cadastro('Gustavo')
pessoa1.cadastrar_nova_pessoa()

pessoa2 = mini_sistema_cadastro('Ana')
pessoa2.cadastrar_nova_pessoa()

pessoa1.listar_pessoas()
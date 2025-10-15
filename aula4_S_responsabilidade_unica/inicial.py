#solid
# S - Responsabilidade Unica / Single Responsability
# modo errado

# Responsabilidade unica seria manter tudo organizado em cada metodo ou função
# esse codigo possui 3 responsabilidades que podem ser unicas
class SistemaCadastral:
    def cadastrar(self, nome: str, idade: int) -> None:
        if isinstance(nome, str) and isinstance(idade, int): # 1
            print('Acessando banco de dados!') # 2
            print(f'Cadastrar usuario {nome}, idade {idade}')
        else:
            print('Dados invalidos!') # 2
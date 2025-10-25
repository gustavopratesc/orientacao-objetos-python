# Autor e Livro:
# Crie classes Autor e Livro. Um autor pode ter vários livros, e cada livro pertence a um autor. Exiba o nome do autor junto ao título do livro.

class Livro:
    def __init__(self, nome: str) -> None:
        self.nome = nome
    
    def livro_formatado(self) -> str:
        return f'Livro: {self.nome}'
    

class Autor:
    def __init__(self, nome):
        self.nome = nome
        self.livros = []

    def adicionar_livro(self, livro: Livro) -> None:
        self.livros.append(livro)

    def mostrar_dados(self) -> None:
        print(f'-- Autor: {self.nome} --')
        for l in self.livros:
            print(l.livro_formatado())



gustavo = Autor('Gustavo')

l1 = Livro('Como treinar python')
l2 = Livro('Estudando python 1 ano')
l3 = Livro('Algoritimos com python')

gustavo.adicionar_livro(l1)
gustavo.adicionar_livro(l2)
gustavo.adicionar_livro(l3)

gustavo.mostrar_dados()
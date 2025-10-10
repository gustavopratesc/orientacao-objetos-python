class Pessoa:
    def __init__(self, nome):
        self.nome = nome
        self.amigos = []

    def adicionar_amigo(self, outro_nome):
        if outro_nome in self.amigos:
            print(f'Essa pessoa ja esta na lista!')
        else:
            self.amigos.append(outro_nome)

    def mostrar_amigos(self):
        if not self.amigos:
            print(f'{self.nome} não possui amigos na lista ainda!')
        else:
            print(f'Amigos de {self.nome}')
            for i, v in enumerate(self.amigos, start=1):
                print(f'{i}: {v}')


pessoa1 = Pessoa('Gustavo')

pessoa1.adicionar_amigo('Ana')
pessoa1.adicionar_amigo('Victor')
pessoa1.adicionar_amigo('Vinicius')
pessoa1.adicionar_amigo('Alisson')
pessoa1.adicionar_amigo('Breno')

pessoa1.mostrar_amigos()
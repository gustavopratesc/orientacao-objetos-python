class Pessoa_Energia:
    def __init__(self, nome):
        self.nome = nome
        self.energia = 100

    def correr(self):
        self.energia -= 10
        print(f'Você correu você reduziu 10 de energia! Energia atual: {self.energia}')

    def dormir(self):
        self.energia += 20
        if self.energia > 100:
            self.energia = 100
        print(f'Dormiu +20 de energia! Energia atual: {self.energia}')

    def comer(self):
        self.energia += 10
        if self.energia > 100:
            self.energia = 100

        print(f'Comeu +10 de energia! Energia Atual: {self.energia}')

    def status(self):
        return {'nome': self.nome, 'energia': self.energia}

pessoa1 = Pessoa_Energia('Gustavo')

pessoa1.comer()
pessoa1.correr()
pessoa1.correr()
pessoa1.correr()
pessoa1.status()
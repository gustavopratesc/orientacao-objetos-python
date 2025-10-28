class Ferramenta:
    def usar(self):
        pass

class Martelo(Ferramenta):
    def usar(self) -> None:
        print('Martelo para bater pregos...')

class Serrote(Ferramenta):
    def usar(self) -> None:
        print('Serrote para serrar...')

class ChavedeFenda(Ferramenta):
    def usar(self) -> None:
        print('Chave de fenda para abrir')

class Construcao:
    def executar(self, ferramenta: Ferramenta) -> None:
        ferramenta.usar()


ex = Construcao()

m = Martelo()
s = Serrote()
c = ChavedeFenda()

ex.executar(m)
ex.executar(s)
ex.executar(c)
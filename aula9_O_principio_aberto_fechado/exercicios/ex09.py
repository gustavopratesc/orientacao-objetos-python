class Personagem:
    def atacar(self) -> None:
        pass

class Guerreiro(Personagem):
    def atacar(self) -> None:
        print('O guerreiro com sua espada ira atacar....')

class Mago(Personagem):
    def atacar(self) -> None:
        print('O mago com seu cajado ira conjurar o ataque!!')

class Arqueiro(Personagem):
    def atacar(self) -> None:
        print('O arqueiro ira atirar suas flechas!')

class Assasino(Personagem):
    def atacar(self) -> None:
        print('O assasino ira andar pelas sombras')

class Dragao(Personagem):
    def atacar(self) -> None:
        print('O dragão irar rosnar fogo!!')

class Batalha:
    def iniciar(self, personagem: Personagem) -> None:
        personagem.atacar()


p = Batalha()

guerreiro = Guerreiro()
mago = Mago()
arqueiro = Arqueiro()
dragao = Dragao()
assasin = Assasino()

p.iniciar(guerreiro)
p.iniciar(mago)
p.iniciar(arqueiro)
p.iniciar(dragao)
p.iniciar(assasin)
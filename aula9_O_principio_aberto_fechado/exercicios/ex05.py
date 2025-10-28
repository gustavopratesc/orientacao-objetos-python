'''classe base'''
class Instrumento:
    def tocar(self) -> None:
        pass


'''sub-clases'''

class Violao(Instrumento):
    def tocar(self) -> None:
        print('O violão esta tocando...')

class Bateria(Instrumento):
    def tocar(self) -> None:
        print('A bateria esta tocando, bum, bum, tuc, paf...')
    
class Piano(Instrumento):
    def tocar(self) -> None:
        print('O piano esta tocando, som calmante.....')

class Guitarra(Instrumento):
    def tocar(self) -> None:
        print('A guitarra esta tocando zuuuuumzaaaammm,...')

# classe principal

class Orquestra:
    def executar(self, instrumento: Instrumento):
        instrumento.tocar()



instrumento = Orquestra()

violao = Violao()
bateria = Bateria()
piano = Piano()
guitarra = Guitarra()

instrumento.executar(violao)
instrumento.executar(bateria)
instrumento.executar(piano)
instrumento.executar(guitarra)
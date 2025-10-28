class Animal:
    def agir(self) -> None:
        pass


class Cachorro(Animal):
    def agir(self) -> None:
        print('O cachorro esta latindo au au au..')


class Gato(Animal):
    def agir(self) -> None:
        print('O gato esta miando, miauu, miauuu...')

class Passaro(Animal):
    def agir(self) -> None:
        print('O passaro esta voando...')


class Zoologico:
    def mostrar_acao(self, animal: Animal) -> None:
        print('O zoologico está animado!!')
        animal.agir()
        print('O publico aplaude!!')
    

animal = Zoologico()

cachorro = Cachorro()
gato = Gato()
passaro = Passaro()

animal.mostrar_acao(cachorro)
animal.mostrar_acao(gato)
animal.mostrar_acao(passaro)

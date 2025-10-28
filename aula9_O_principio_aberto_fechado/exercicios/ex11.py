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

class ShowDeAnimais:
    def iniciar_show(self, animais: list):
        for animal in animais:
            animal.agir()

class Zoologico:
    def mostrar_acao(self, animal: Animal) -> None:
        print('O zoologico está animado!!')
        animal.agir()
        print('O publico aplaude!!')
    

animal = Zoologico()
teste = ShowDeAnimais()
animais_no_show = [Cachorro(), Gato(), Passaro()]

teste.iniciar_show(animais_no_show)
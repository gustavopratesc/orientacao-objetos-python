# Maneira correta do principio aberto e fechado!
'''
Definição:
Uma classe deve estar aberta para extensão, mas fechada para modificação.

Em outras palavras:

Aberta para extensão: você deve conseguir adicionar novos comportamentos à classe sem alterá-la diretamente.

Fechada para modificação: o código existente não deve precisar ser modificado para que novas funcionalidades funcionem.
'''

class Artista:
    def __init__(self, tipo: str) -> None:
        self.tipo = tipo

    def apresentar_show(self) -> None:
        print(f'O {self.tipo} esta apresentando seu show!')

class Circo:
    def apresentar(self, artista: Artista) -> None:
        print('O circo esta abrindo!')
        artista.apresentar_show()
        print('A plateia aplaude!!')
'''
Aqui, o método apresentar do Circo não precisa mudar se você quiser adicionar novos artistas.
Basta criar uma nova classe derivada de Artista, e o sistema continua funcionando.
Ou seja, o código está aberto para extensão (você cria novos artistas) e fechado para modificação (não altera o Circo).
'''
circo = Circo()
# nesse codigo você cria os artistas sem modificar o metodo principal sem intervir para mudanças
palhaco = Artista('Palhaço')
magico = Artista('Magico')

circo.apresentar(palhaco)
print('----------')
circo.apresentar(magico)

# Maneira errada!

class Circo:
    def apresentar(self, command: int) -> None:
        if command == 1:
            self.__show_palhaco() # isso fere o principio aberto e fechado pois se precisar criar mais artistas acaba que você tem que entrar no metodo principal interromper e adicionar um novo!
        if command == 2:
            self.__show_malabarista()

    def __show_palhaco(self):
        print(f'O palhaço esta apresentando seu show')

    def __show_malabarista(self):
        print(f'O malabarista esta apresentando seu show')

circo = Circo()

command = 2
circo.apresentar(command)
class Celular:
    def __init__(self, modelo: str) -> None:
        self.modelo = modelo

    def enviar_mensagem(self, mensagem: str) -> None:
        print(f'Enviando mensagem: {mensagem}')

    def abrir_emais(self) -> None:
        print('Abrindo emails...')

    def abrir_youtube(self) -> None:
        print('Abrindo youtube...')

    
class Pessoa:
    def __init__(self, celular: Celular) -> None:
        self.__celular = celular

    def pedir_pizza(self) -> None:
        print('Buscando o celular..')
        print('Definindo o sabor....')
        self.__celular.enviar_mensagem('Quero pizza 4 queijos')
        print('aguardando chegada')

    def estudar(self) -> None:
        print('Sentando no computador')
        self.__celular.abrir_youtube()
        print('Anotando o conteudo')

android = Celular('Samsumg')
iphone = Celular('Iphone')
        
gustavo = Pessoa(iphone)
jose = Pessoa(android)

gustavo.pedir_pizza()
print()
jose.estudar()
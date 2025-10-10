# metodos privados
# quando tem dois __ <- significa que é privado
class Pessoa:
    def __init__(self, altura, cpf) -> None:
        self.altura = altura
        self.__cpf = cpf

    def apresentar(self):
        print(f'Olá minha altura é {self.altura}')
        self.__coletar_documento()

    def __coletar_documento(self):
        print(f'Meu documento {self.__cpf}')


gustavo = Pessoa(1.70, 71066839140)

'''maneira dos atributos'''

#print(gustavo.__cpf) # da erro porque __cpf é um atributo privado e não pode ser acessado diretamento pelo objeto

# maneira de chamar

gustavo.apresentar() # aqui tem um metodo e dentro desse metodo tem outro metodo privado que tem o print com o __cpf

'''maneira dos metodos'''

gustavo.__coletar_documento() # da erro porque é um metodo privado

# maneira correta

gustavo.apresentar() # aqui é tem dentro o metodo self.__coletar_documento() ai tem como aparecer

class Funcionario:
    def __init__(self, nome, salario) -> None:
        self.nome = nome
        self.__salario = salario

    def mostrar_informacoes(self):
        print(f'Seu nome é {self.nome}')
        self.__mostrar_salario()

    def __mostrar_salario(self):
        print(f'Salario R$ {self.__salario}')


pessoa1 = Funcionario('Gustavo', 1520)

pessoa1.mostrar_informacoes()


        
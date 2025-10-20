class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.__salario = salario


    def mostrar_dados(self) -> str:
        return f'''
        Nome: {self.nome}
        Salario: {self.__mostrar_salario()}
'''

    def __mostrar_salario(self) -> float:
        return self.__salario
        

pessoa1 = Funcionario('Gustavo', 1500)

print(pessoa1.mostrar_dados())
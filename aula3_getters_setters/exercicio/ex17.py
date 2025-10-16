class Funcionario:
    def __init__(self, nome, salario):
        self.__nome = nome
        self.__salario = salario

    @property
    def salario(self):
        return f'Funcionario: {self.__nome} | R${self.__salario:.2f}'
    
    @salario.setter
    def definir_salario(self, valor):
        if valor < 1412:
            raise ValueError('ERRO: Insira valores acima de 1412')
        else:
            self.__salario = valor

funcionario1 = Funcionario('Gusstavo', 1500)

print(funcionario1.salario)

funcionario1.definir_salario = 2500

print(funcionario1.salario)


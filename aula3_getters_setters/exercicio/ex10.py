class ContaBancaria:
    def __init__(self):
        self.__saldo = 0

    @property
    def conta(self):
        return f'R${self.__saldo:.2f}'
    
    @conta.setter
    def definir_saldo(self, valor):
        if isinstance(valor, (int, float)) and valor > 0:
            self.__saldo = valor
        else:
            raise ValueError('ERRO: Insira apenas números inteiros')


usuario = ContaBancaria()

usuario.definir_saldo = 500
print('Saldo atual:',usuario.conta)
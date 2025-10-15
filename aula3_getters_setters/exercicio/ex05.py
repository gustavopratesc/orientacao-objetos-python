class Conta:
    def __init__(self, titular) -> None:
        self.titular = titular
        self.__saldo = 0

    @property
    def saldo(self) -> float:
        return self.__saldo
    
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print('ERRO: Insira números positivos!')

    def sacar(self, valor):
        if valor > self.__saldo or valor < 0:
            print('ERRO: Saque insuficiente!')
        else:
            self.__saldo -= valor
            print(f'Valor sacado: {valor}')


pessoa1 = Conta('Gustavo')

print(f'Seu saldo atual: {pessoa1.saldo}')
pessoa1.depositar(2000)
print(f'Seu saldo atual: {pessoa1.saldo}')
pessoa1.sacar(2550)
print(f'Seu saldo atual: {pessoa1.saldo}')


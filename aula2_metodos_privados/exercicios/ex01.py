class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo

    def depositar(self, valor):
        self.__saldo += valor
        print(f'Valor adicionado ao saldo: R${valor}')

    def __mostrar_valor(self):
        print(f'Saldo atual R${self.__saldo}')

    def ver_extrato(self):
        self.__mostrar_valor()

pessoa1 = ContaBancaria('Gustavo', 1500)

pessoa1.depositar(500)

pessoa1.ver_extrato()
        
class ContaCorrente:
    def __init__(self, titular, saldo):
        self.titular = titular
        try:
            self.__saldo = float(saldo)
        except ValueError:
            print('ERRO: Insira apenas valores númericos!')
            self.__saldo = None

    def depositar(self, valor):
        if self.__saldo is None:
            print('Operação invalida: saldo indefinido!')
            return

        if valor <= 0:
            print('ERRO: Valor inserido invalido!')
        else:
            self.__saldo += valor
            print(f'Foi depositado R${valor:.2f} a conta!')
    
    def sacar(self, valor):
        if self.__saldo is None:
            print(f'Operação invaida: saldo indefinido!')
            return

        if self.__validar_saque(valor):
            self.__saldo -= valor
            print(f'Você sacou R${valor:.2f}')
        else:
            print(f'Saldo insuficiente!')

    def __validar_saque(self, valor):
        if valor <= self.__saldo:
            return True
        
    def ver_saldo(self):
        if self.__saldo is not None:
            print(f'Saldo atual de {self.titular}: R${self.__saldo:.2f}')
        else:
            print('Saldo indisponivel')
    

pessoa1 = ContaCorrente('Gustavo', 1500)

pessoa1.ver_saldo()
pessoa1.sacar(300)
pessoa1.ver_saldo()
pessoa1.depositar(2000)
pessoa1.ver_saldo()
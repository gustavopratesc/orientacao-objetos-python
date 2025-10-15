class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self.__senha = 12345

    def __autenticar(self, senha):
        return self.__senha == senha
    
    def depositar(self, senha, valor):
        if self.__autenticar(senha):
            self.saldo += valor
            print(f'Deposito feito com sucesso! R${valor}')
        else:
            print(f'Senha incorreta')

    def sacar(self, senha, valor):
        if self.__autenticar(senha):
            self.saldo -= valor
            print(f'Saque feito com sucesso! Valor: R${valor}')
        else:
            print('Senha incorreta!')
    
    def mostrar_saldo(self):
        print(f'Saldo atual: R${self.saldo}')

pessoa1 = ContaBancaria('Gustavo', 1500)
pessoa1.mostrar_saldo()
pessoa1.depositar(12345, 1500)
pessoa1.mostrar_saldo()
pessoa1.sacar(12345, 1322)
pessoa1.mostrar_saldo()
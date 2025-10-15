class Conta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo


    def ver_saldo(self):
        print(f'Titular: {self.titular} | Saldo: R${self.saldo}')


pessoa1 = Conta('Gustavo', 100)

pessoa1.ver_saldo()
        
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor < 0:
            print('ERRO: Valor inserido não pode ser depositado')
        else:
            self.saldo += valor
            print(f'Depositado o valor de R${valor}')
        
    def sacar(self, valor):

        if valor > self.saldo:
            print('ERRO: Valor muito alto')
        else:
            self.saldo -= valor
            print(f'Valor sacado R${valor}')

    def ver_saldo(self):
        print(f'Saldo atual: R${self.saldo}')


conta1 = ContaBancaria('Gustavo', 1500)

conta1.ver_saldo()
conta1.depositar(200)
conta1.ver_saldo()
conta1.sacar(500)
conta1.ver_saldo()
conta1.sacar(2000)

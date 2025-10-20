class ContaBancaria:
    taxa_juros = 0.05

    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def aplicar_juros(self):
        juros = (self.saldo * self.taxa_juros)
        print(f'Juros aplicado: {juros}')

p1 = ContaBancaria('Gustavo', 1500)
p2 = ContaBancaria('Gustavo', 3500)
ContaBancaria.taxa_juros = 0.02
p1.aplicar_juros()
p2.aplicar_juros()
class ContaBancaria:
    def __init__(self):
        self.__saldo = 1500

    
    def depositar(self, valor):
        self.__saldo += valor
        print(f'Valor R${valor} depositado com sucesso!')
        self.__registrar_operacao()

    

    def __registrar_operacao(self):
        
        print(f'Operação registrada no sistema!')


usuario1 = ContaBancaria()

usuario1.depositar(1500)
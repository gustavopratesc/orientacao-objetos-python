class ContaPremium:
    def __init__(self):
        self.__saldo = 1500
        self.__limite = 1000
        self.__senha = 123

    def depositar(self, valor, senha):
        if self.__autenticar_senha(senha):
            self.__saldo += valor
            print(f'Valor depositado: R${valor}')
        else:
            print('Credenciais invalidas!')

    def sacar(self, valor, senha):
        if self.__autenticar_senha(senha):
            self.__saldo -= valor
            print(f'Valor sacado: R${valor}')
        else:
            print('Credenciais invalidas!')

    def definir_limite(self, valor, senha):
        if self.__autenticar_senha(senha):
            self.__limite = valor
            print(f'Limite definido para: {self.__limite}')
        else:
            print('Credenciais invalidas!')

    def mostrar_informacoes(self, senha):
        if self.__autenticar_senha(senha):
            print(f'Saldo: R${self.__saldo}')
            print(f'Limite: R${self.__limite}')
        else:
            print('Credenciais invalidas!')

    def __autenticar_senha(self, senha):
        return self.__senha == senha

usuario = ContaPremium()

usuario.mostrar_informacoes(123)
usuario.depositar(1500, 123)
usuario.mostrar_informacoes(123)

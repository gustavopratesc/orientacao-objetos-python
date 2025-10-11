class Cofre:
    def __init__(self, senha, valor_guardado):
        self.__senha = senha
        self.__valor_guardado = valor_guardado

    def depositar(self, valor, senha):
        if self.__verificar_senha(senha):
            self.__valor_guardado += valor
            print(f'Valor depositado R${valor:.2f} com sucesso!')
        else:
            print('Não é possivel depositar senha errada!')

    def __verificar_senha(self, senha):
        return senha == self.__senha
        
    def ver_saldo(self, senha):
        if self.__verificar_senha(senha):
            print(f'Valor guardado: R${self.__valor_guardado}')
        else:
            print('Não é possivel ver')
        

pessoa1 = Cofre(12345, 1500)

pessoa1.ver_saldo(12345)
pessoa1.depositar(3000, 12345)
pessoa1.ver_saldo(12345)
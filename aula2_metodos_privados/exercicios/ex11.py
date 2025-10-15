class Cofre:
    def __init__(self, valor):
        self.__senha = 817981
        self.valor = valor

    
    def abrir(self, senha):
        if self.__verificar_senha(senha):
            print(f'Senha esta correta!')
            print(f'Cofre aberto, valor disponivel R${self.valor:.2f}')
        else:
            print(f'Senha incorreta. Acesso negado!')
    
    def __verificar_senha(self, senha):
        return self.__senha == senha
    

pessoa1 = Cofre(1500)

pessoa1.abrir(817981)
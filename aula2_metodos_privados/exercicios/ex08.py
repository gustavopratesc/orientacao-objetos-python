class Elevador:
    def __init__(self, andar_atual):
        self.andar_atual = andar_atual
        self.__andar_maximo = 15
        self.__senha_manutencao = 12345

    def subir(self):
        print(f'Subiu ate {self.__andar_maximo}, o maximo do andar do predio!')

    def __modo_manutencao(self, senha):
        if senha == self.__senha_manutencao:
            print('Modo manutenção ativado')
        else:
            print('Senha errada!')

    def ativar_manutencao(self, senha):
        self.__modo_manutencao(senha)


teste1 = Elevador(5)

teste1.subir()
teste1.ativar_manutencao(12345)
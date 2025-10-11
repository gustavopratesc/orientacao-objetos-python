class Servidor:
    def __init__(self, nome, chave_acesso):
        self.nome = nome
        self.__chave_acesso = chave_acesso
        self.__dados_confidenciais = 'Oi tudo bem?'

    def __autenticar_chave(self, chave):
        return chave == self.__chave_acesso
    
    def acessar_dados(self, chave):
        if self.__autenticar_chave(chave):
            print(f'Os dados confidenciais: {self.__dados_confidenciais}')
        else:
            print('Acesso negado!')

    def modificar_dados(self, chave, novos_dados):
        if self.__autenticar_chave(chave):
            self.__dados_confidenciais = novos_dados
            print(f'Dados alterados com sucesso!')
        else:
            print('Acesso negado!')


usuario1 = Servidor('Gustavo', 12345)

usuario1.acessar_dados(12345)
usuario1.modificar_dados(12345, 'Tudo bem e você?')
usuario1.acessar_dados(12345)
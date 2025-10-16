class GeradorRelatorio:
    def gerar(self, dados: list) -> None:
        if self.__coletar_dados(dados):
            dados_formatados = self.__formatar_dados(dados)
            self.__exibir_relatorio(dados_formatados)
        else:
            print(f'Nenhum dado valido foi encontrado!')

    #

    def __coletar_dados(self, dados: list) -> bool:
        return isinstance(dados, list) and len(dados) > 0

    def __formatar_dados(self, dados: list) -> str:
        print(f'Formatando dados')
        relatorio = '\n'.join([f'- {item}' for item in dados])
        return relatorio

    def __exibir_relatorio(self, relatorio_formatado: str) -> None:
        print(f'Relatorio gerado com sucesso!')
        print('-' * 30)
        print(relatorio_formatado)
        print('-' * 30)
    

dados = ['Usuario: Gustavo', 'Idade: 21', 'Cargo: Estudante de SI', 'Interesse em back-end Python']

relatorio = GeradorRelatorio()

relatorio.gerar(dados)
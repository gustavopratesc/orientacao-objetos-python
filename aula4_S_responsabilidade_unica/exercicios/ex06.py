class Pagamento:
    def __init__(self, valor):
        self.valor = valor

    def pagamento(self):
        if self.__validar_valor(self.valor):
            self.__procesar_pagamento()
            self.__exibir_confirmacao()
        else:
            self.__validar_erro()

    #

    def __validar_valor(self, valor) -> bool:
        return isinstance(valor, (float, int)) and valor > 0
    

    def __procesar_pagamento(self) -> None:
        print('Processando pagamento...')

    def __exibir_confirmacao(self):
        while True:
            c = str(input('Quer confirmar pagamento? [S/N]: ')).strip().upper()
            if c in ['N', 'NÃO', 'N']:
                print('Pagamento cancelado!')
                return
            elif c in ['S', 'SIM']:
                print('Pagamento efetuado com sucesso!')
                return
            else:
                print('Digite entre [S/N]!')

    def __validar_erro(self):
        print('ERRO: Insira valores númericos maiores que 0')


usuario1 = Pagamento(120)

usuario1.pagamento()
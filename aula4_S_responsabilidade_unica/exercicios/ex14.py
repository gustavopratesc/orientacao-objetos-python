class ContaBancaria:

    def __init__(self, titular, saldo=0) -> None:
        self.__titular = titular
        self.__saldo = saldo
        self.__historico = []

    def depositar(self, valor: float) -> str:
        if self.__validar_valor(valor):
            self.__saldo += valor
            self.__registrar_transacao('Deposito', valor)
            return f'Valor R${valor} depositado com sucesso!'
        else:
            self.__validar_erro()

    def sacar(self, valor: float) -> str:
        if not self.__validar_valor(valor):
            return self.__validar_erro()
        
        if valor > self.__saldo:
            return f'Saldo insuficiente'
        
        self.__saldo -= valor
        self.__registrar_transacao('Saque', valor)
        return f'Saque de R${valor:.2f} realizado com sucesso!'

    def ver_extrato(self):
        if not self.__historico:
            return f'Extrato de {self.__titular}\n Nenhuma transação realizada ainda'
        
        resultado = f'Extrato de {self.__titular}\n------------------------\n'
        for transacao in self.__historico:
            tipo = transacao["tipo"]
            valor = transacao["valor"]
            sinal = '+' if tipo == 'Deposito' else '-'
            resultado += f'{sinal} R${valor:.2f} ({tipo})\n'
        
        resultado += '----------------------\n'
        resultado += f'Saldo atual: R${self.__saldo:.2f}'
        return resultado

    def __validar_valor(self, valor: float) -> bool:
        return isinstance(valor, (int, float)) and valor > 0

    def __registrar_transacao(self, tipo: str, valor: float) -> str:
        self.__historico.append({'tipo': tipo, 'valor': valor})
    
    def __validar_erro(self):
        return f'ERRO: Insira dados corretos!'
    

usuario1 = ContaBancaria('Gustavo', 1500)

print(usuario1.ver_extrato())

print(usuario1.depositar(1500))
print(usuario1.ver_extrato())
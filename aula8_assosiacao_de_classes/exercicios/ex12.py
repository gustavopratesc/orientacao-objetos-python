# Conta Bancária e Transações:
# Crie uma classe Conta com número e saldo, e uma classe Transacao com tipo (saque/deposito) e valor. Cada conta deve ter uma lista de transações associadas.
class Transacao:
    def __init__(self, tipo: str, valor) -> None:
        self.tipo = tipo
        self.valor = valor
    
    def exibir(self) -> str:
        return f'Tipo {self.tipo.capitalize()} | Valor R${self.valor:.2f}'

class Conta:
    def __init__(self, numero: int, saldo: float = 0.0) -> None:
        self.numero = numero
        self.saldo = saldo
        self.lista = []

    def registrar_transacao(self, transacao: Transacao) -> None:
        if transacao.tipo in ['saque', 'SAQUE', 'Saque'] and transacao.valor <= self.saldo:
            self.saldo -= transacao.valor
        elif transacao.tipo in ['deposito', 'DEPOSITO', 'Deposito']:
            self.saldo += transacao.valor
        else:
            print(f'ERRO: saldo insuficiente para saque')
            return
        
        self.lista.append(transacao)

    def extrato(self) -> None:
        print(f'--- Extrato de Conta {self.numero} ---')
        for t in self.lista:
            print(t.exibir())
        print(f'Saldo atual R${self.saldo:.2f}')
        print('---------------------------------')

c1 = Conta(12345, 1000)

t1 = Transacao('depósito', 500)
t2 = Transacao('saque', 200)
t3 = Transacao('saque', 1500)  # saldo insuficiente

c1.registrar_transacao(t1)
c1.registrar_transacao(t2)
c1.registrar_transacao(t3)

c1.extrato()  

## ou


class Transacao:
    def __init__(self, tipo: str, valor: float) -> None:
        self.tipo = tipo
        self.valor = valor
    
    def exibir(self) -> str:
        return f'Tipo: {self.tipo.capitalize()} | Valor: R${self.valor:.2f}'


class Conta:
    def __init__(self, numero: int, saldo: float = 0.0) -> None:
        self.numero = numero
        self.saldo = saldo
        self.lista = []  # lista de transações

    def registrar_transacao(self, transacao: Transacao) -> None:
        if transacao.tipo.lower() == 'saque' and transacao.valor <= self.saldo:
            self.saldo -= transacao.valor

        elif transacao.tipo.lower() in ['depósito', 'deposito']:
            self.saldo += transacao.valor

        else:
            print('⚠️ ERRO: saldo insuficiente para saque.')
            return
        
        self.lista.append(transacao)

    def extrato(self) -> None:
        print(f'\n--- Extrato da Conta {self.numero} ---')
        for t in self.lista:
            print(t.exibir())
        print(f'Saldo atual: R${self.saldo:.2f}')
        print('---------------------------------')


# --- Teste ---
c1 = Conta(12345, 1000)

t1 = Transacao('depósito', 500)
t2 = Transacao('saque', 200)
t3 = Transacao('saque', 1500)  # saldo insuficiente

c1.registrar_transacao(t1)
c1.registrar_transacao(t2)
c1.registrar_transacao(t3)

c1.extrato()

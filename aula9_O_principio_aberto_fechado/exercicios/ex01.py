# Princípio básico

# Objetivo: usar o mesmo método com comportamentos diferentes sem alterar o código principal.

# Exercício:
# Crie uma classe Imposto e subclasses ImpostoRenda, IPTU e ISS, cada uma com um método calcular(valor).
# Depois, crie uma classe CalculadoraDeImpostos que recebe qualquer tipo de imposto e calcula o valor total sem precisar saber qual imposto é.

class Imposto:
    def calcular(self, valor: float) -> None:
        raise NotImplemented('A subclasse deve implementar esse metodo!')

# subclasses

class ImpostoRenda(Imposto):
    def calcular(self, valor: float) -> float:
        return valor * 0.15
    
class IPTU(Imposto):
    def calcular(self, valor: float) -> float:
        return valor * 0.05
    
class ISS(Imposto):
    def calcular(self, valor: float) -> float:
        return valor * 0.1
    

class CalculadoraDeImposto:
    def calcular_imposto(self, imposto: Imposto, valor: float) -> None:
        total = imposto.calcular(valor)
        print(f'Valor base: R${valor:.2f}')
        print(f'Imposto calculado ({imposto.__class__.__name__}: R${total:.2f})')
        print(f'Total com imposto R${valor + total:.2f}\n')
        


imposto_renda = ImpostoRenda()
iptu = IPTU()
iss = ISS()

# Criando a calculadora
calculadora = CalculadoraDeImposto()

# Testando com diferentes impostos
calculadora.calcular_imposto(imposto_renda, 1000)
calculadora.calcular_imposto(iptu, 5000)
calculadora.calcular_imposto(iss, 2000)
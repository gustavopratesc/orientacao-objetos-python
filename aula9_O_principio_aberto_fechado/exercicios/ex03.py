# Classe base genérica
class Transporte:
    def mover(self) -> None:
        """Método genérico que será sobrescrito pelas subclasses"""
        pass


# Subclasses específicas (cada uma com seu comportamento próprio)
class Carro(Transporte):
    def mover(self) -> None:
        print("🚗 O carro está andando na estrada!")


class Aviao(Transporte):
    def mover(self) -> None:
        print("✈️ O avião está voando pelos céus!")


class Navio(Transporte):
    def mover(self) -> None:
        print("🚢 O navio está navegando pelo mar!")


# Classe principal (fechada para modificação)
class Viagem:
    def iniciar(self, transporte: Transporte) -> None:
        print("🌍 Iniciando a viagem...")
        transporte.mover()
        print("✅ Viagem concluída!\n")


# Testando o sistema
viagem = Viagem()

carro = Carro()
aviao = Aviao()
navio = Navio()

viagem.iniciar(carro)
viagem.iniciar(aviao)
viagem.iniciar(navio)

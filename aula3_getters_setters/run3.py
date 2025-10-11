class MinhaClasse:
    def __init__(self) -> None:
        self.__valor = None  # atributo privado

    @property
    def valor(self) -> int:
        """Getter - permite acessar __valor como se fosse um atributo comum"""
        return self.__valor

    @valor.setter
    def valor(self, novo_valor: int) -> None:
        """Setter - controla como __valor pode ser modificado"""
        if isinstance(novo_valor, int) and novo_valor >= 0:
            self.__valor = novo_valor
        else:
            print("ERRO: O valor deve ser um número inteiro positivo!")

# -------------------------------
# Testando a classe
# -------------------------------

obj = MinhaClasse()

obj.valor = 42         # Chama automaticamente o setter
print(obj.valor)       # Chama automaticamente o getter

obj.valor = -10        # Tenta definir um valor inválido
print(obj.valor)       # Continua com o valor anterior (42)

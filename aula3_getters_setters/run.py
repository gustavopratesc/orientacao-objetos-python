class MinhaClasse:
    def __init__(self) -> None: # vai retornar anda vai printar nada
        # self.valor = None
        self.__valor = None
        self.__elem = None

    def setter_valor(self, valor: int) -> None: # vai retornar anda vai printar nada
        self.__valor = valor
    
    def getter_valor(self) -> int:
        return self.__valor

my_class = MinhaClasse(15)
# my_class.__valor = 3 # ferindo o encapsulamento
# print(my_class.__valor)

my_class.setter_valor(42) # vai setar o valor como 42
valor = my_class.getter_valor() # vai retornar o valor
print(valor)
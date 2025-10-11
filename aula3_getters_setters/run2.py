class MinhaClasse:
    def __init__(self) -> None: # vai retornar anda vai printar nada
        # self.valor = None
        self.__valor = None
        self.__elem = None
    
    def setter_valor(self, valor: int) -> None: # vai retornar anda vai printar nada
        self.__valor = valor
    
    @property
    def getter_valor(self) -> int:
        return self.__valor

my_class = MinhaClasse()
my_class.setter_valor(123)
print(my_class.getter_valor)
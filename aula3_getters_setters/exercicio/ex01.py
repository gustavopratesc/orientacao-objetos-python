class Pessoa:
    def __init__(self) -> None:
        self.__idade = None

    @property
    def idade(self) -> int:
        return self.__idade

    @idade.setter
    def idade(self, nova_idade):
        if isinstance(nova_idade, int) and 0 <= nova_idade <= 120:
            self.__idade = nova_idade
        else:
            print('ERRO: Insira uma idade valida!')


pessoa1 = Pessoa()

pessoa1.idade = 21
print(f'Sua idade é:',pessoa1.idade)
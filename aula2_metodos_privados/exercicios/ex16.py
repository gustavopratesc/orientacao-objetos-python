class CofreDigital:
    def __init__(self):
        self.__senha = 8179815710
        self.__tentativas = 3
        self.__bloqueado = False

    
    def abrir(self, senha):
        if self.__bloqueado == False:
            print('Cofre bloqueado!')

        if senha != self.__senha:
            self.__tentativas -= 1
            print(f'Senha errada! Tentativas {self.__tentativas}')
        else:
            self.__bloqueado = True
            print('Cofre Aberto!')
        
        if self.__tentativas == 0:
            self.__bloquear()
            return
        
    def __bloquear(self):
        print(f'O cofre esta bloqueado!')

usuario2 = CofreDigital()

usuario2.abrir(8179815710)



        
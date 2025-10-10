class MinhaClasse:
    def __init__(self, info, elem): # oq é __init__ <- metodo construtor, metodo que roda primeiro do que os outros de baixo, primeiro metodo a executar
        self.atributo_1 = 'Meu atributo'
        self.atributo_2 = elem # pode ser qualquer coisa
        self.atributo_3 = [1, 2, 'a']
        self.atributo_novo = info 
        print(self.atributo_novo)

    def metodo1(self):
        print('Minha ação 1')
        print('Minha ação 2')
        print(self.atributo_2)
        return 'Hello World' # o return so pega se criar uma variavel

    def metodo2(self, numero):
        self.metodo1()
        print(self.atributo_3[1] + numero)

# objeto       # classe -> instaciamos um objeto
minha_classe = MinhaClasse('Info aqui no construtor', '213')

# objeto que realiza a ação
minha_classe.metodo1()

minha_classe.metodo2(10)
# cria uma variavel que coloca o objeto que realiza a ação para depois printar
# response = minha_classe.metodo1()

# print(response)


## fazer uma classe pessoa como exercicio
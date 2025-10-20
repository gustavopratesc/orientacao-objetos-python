class AppConfig:
    ambiente = 'Desenvolvimento'

    def __init__(self):
        self.estado = 'oi'

    @classmethod
    def definir_ambiente_producao(cls):
        cls.ambiente = "Produção"

    def mostrar_status(self):
        print(self.ambiente)


teste = AppConfig()

teste.mostrar_status()

AppConfig.definir_ambiente_producao()

teste.mostrar_status()
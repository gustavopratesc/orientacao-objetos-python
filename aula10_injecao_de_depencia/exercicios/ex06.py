class Notificacao:
    def enviar(self):
        pass

class NotificacaoEmail(Notificacao):
    def enviar(self):
        print('Notificação de email')

class NotificacaoSms(Notificacao):
    def enviar(self):
        print('SMS no seu correiro')

class NotificacaoPush(Notificacao):
    def enviar(self):
        print('Notificação push')

class Aplicativo:
    def __init__(self, nome_app: str, noticacao: Notificacao):
        self.nome_app = nome_app
        self.__notificaco = noticacao

    def notificar_usuario(self):
        print(f'O {self.nome_app} esta alertando!!')
        self.__notificaco.enviar()

email = NotificacaoEmail()
sms = NotificacaoSms()
push = NotificacaoPush()

gmail = Aplicativo('Gmail', email)
contatos = Aplicativo('SMS', sms)
o_push = Aplicativo('Push', push)


gmail.notificar_usuario()
contatos.notificar_usuario()
o_push.notificar_usuario()
        
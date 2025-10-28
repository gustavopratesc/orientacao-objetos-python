# class Mensagem:
#     def __init__(self, enviar) -> None:
#         self.enviar = enviar

#     def enviar_mensagem(self) -> None:
#         print(f'Mensagem enviada atraves de: {self.enviar}')

# class SistemaDeMensagens:
#     def disparar(self, mensagem: Mensagem):
#         print('Enviando...')
#         mensagem.enviar_mensagem()

# email = Mensagem('Email')
# sms = Mensagem('SMS')
# notificacao_push = Mensagem('Notificação Push')
# whatsApp = Mensagem('WhatsApp')

# msg = SistemaDeMensagens()

# msg.disparar(email)
# msg.disparar(sms)
# msg.disparar(notificacao_push)
# msg.disparar(whatsApp)

# versão escalonavel

#classe base
class Mensagem:
    def enviar(self) -> None:
        pass

#sub_classes

class Email(Mensagem):
    def enviar(self) -> None:
        print('Email enviado!')

class Sms(Mensagem):
    def enviar(self):
        print('Sms enviado com sucesso!')

class NotificacaoPush(Mensagem):
    def enviar(self):
        print('Noficação push enviada!')

class WhatsApp(Mensagem):
    def enviar(self):
        print('Enviada atraves do wpp')

# classe principal que não pode ser modificada nem alterada

class SistemadeMensagens:
    def disparar(self, mensagem: Mensagem):
        mensagem.enviar()


sistema = SistemadeMensagens()

email = Email()
sms = Sms()
notificacao_push = NotificacaoPush()
wpp = WhatsApp()

sistema.disparar(email)
sistema.disparar(sms)
sistema.disparar(notificacao_push)
sistema.disparar(wpp)
class ServicoMensagem:
    def formatacao(self, destinatario: str, conteudo: str) -> None:
        print(f'{destinatario} estou enviando: {conteudo}')

class Usuario:
    def __init__(self, msg: ServicoMensagem) -> None:
        self.__msg = msg

    def enviar_mensagem(self) -> None:
        print('Enviando mensagem...')
        self.__msg.formatacao('Jose', 'Estou testando poo python')
        print('Finalizando mensagem')

class EmailService(ServicoMensagem):
    def formatacao(self, destinatario: str, conteudo: str) -> None:
        print(f'[E-MAIL] enviado a {destinatario} com conteudo: {conteudo}')

class SmsService(ServicoMensagem):
    def formatacao(self, destinatario: str, conteudo: str):
        print(f'SMS: enviado para {destinatario} com conteudo: {conteudo}')

msg = ServicoMensagem()

email = EmailService()
sms = SmsService()



gustavo = Usuario(email)
joao = Usuario(sms)

gustavo.enviar_mensagem()
joao.enviar_mensagem()    
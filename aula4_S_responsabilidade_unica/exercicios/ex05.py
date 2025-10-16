class EmailService:
    def __init__(self, destinatario, assunto, mensagem):
        self.destinatario = destinatario
        self.assunto = assunto
        self.mensagem = mensagem

    def enviar_email(self):
        if self.__validar_email(self.destinatario):
            self.__corpo_email(self.destinatario, self.assunto, self.mensagem)
            self.__enviando_mensagem(self.destinatario)
        else:
            self.__validando_erro()

    #

    def __validar_email(self, destinatario: str) -> bool:
        if isinstance(destinatario, str):
            return '@' in destinatario and '.com' in destinatario
        else:
            return False
    
    def __corpo_email(self, destinatario: str, assunto: str, mensagem: str) -> None:
        print(f'Email de: {destinatario}')
        print(f'Assunto: {assunto}')
        print(f'-' * 30)
        print(f'{mensagem}')
    
    def __enviando_mensagem(self, destinatario: str) -> None:
        print(f'Enviado email para {destinatario}')

    def __validando_erro(self):
        print('❌ ERRO: Endereço de e-mail inválido!')
    

email_destinatario = input('Insira o email do destinatario: ').strip()
assunto = input('Insira o assunto: ').strip()
mensagem = input('Insira a mensagem: ').strip()

email1 = EmailService(email_destinatario, assunto, mensagem)

email1.enviar_email()
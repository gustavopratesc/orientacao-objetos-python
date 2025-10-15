import re
import hashlib

class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

    
    def registrar(self):
        if not self.__validar_email():
            print('E-mail invalido. Tente novamente')
            return
        
        self.__criptografar_senha()
        print('Usuario cadastrado com sucesso')

    def __validar_email(self):
        print('Validando email...')
        padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(padrao, self.email) is not None
    
    def __criptografar_senha(self):
        print('Validando senha..')
        self.senha = hashlib.sha256(self.senha.encode()).hexdigest()

user1 = Usuario('Gustavo', 'gustavoprates.c@gmail.com', '8179815710Gu')
user1.registrar()
class pessoa:
    def __init__(self, nome, idade, altura, cor_olhos, cor_cabelo, cor_pele):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.cor_olhos = cor_olhos
        self.cor_cabelo = cor_cabelo
        self.cor_pele = cor_pele
    
    def correr(self):
        print(f'{self.nome} esta correndo!!')

    def comer(self):
        print(f'{self.nome} esta comendo!!')

    def exibir_informacoes(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        print(f'Altura: {self.altura}')
        print(f'Cor olhos: {self.cor_olhos}')
        print(f'Cor cabelo: {self.cor_cabelo}')
        print(f'Cor pele: {self.cor_pele}')

nome = str(input('Insira seu nome: ')).strip().title()
try:
    idade = int(input('Insira sua idade: '))
    altura = float(input('Insira sua altura: '))
except ValueError:
    print('ERRO: Valor inserido não é númerico!')

cor_olhos = str(input('Insira a cor dos olhos: ')).strip()
cor_cabelo = str(input('Insira a cor do cabelo: ')).strip()
cor_pele = str(input('Insira a cor de pele: ')).strip()

pessoa1 = pessoa(nome, idade, altura, cor_olhos, cor_cabelo, cor_pele)

pessoa1.exibir_informacoes()
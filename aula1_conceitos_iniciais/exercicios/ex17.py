class Carrinho:
    def __init__(self, nome_cliente):
        self.nome_cliente = nome_cliente
        self.lista = []


    def adicionar_item(self, nome, preco):
        return self.lista.append((nome, preco))
    
    def mostrar_total(self):
        soma = sum(preco for _, preco in self.lista)
        return f'Preço total dos itens R${soma:.2f}'
    
import sys

nome_cliente = str(input('Insira seu nome: ')).strip().title()
if not nome_cliente.replace(' ', '').isalpha():
    raise ValueError('ERRO: Insira um nome valido!')

cliente1 = Carrinho(nome_cliente)

while True:
    nome_item = str(input('Insira o nome do produto: ')).strip().capitalize()
    if not nome_item.replace(' ', '').isalpha():
        raise ValueError('ERRO: Insira um nome valido!')
    
    try:
        preco = float(input('Insira o preço do produto: '))
        cliente1.adicionar_item(nome_item, preco)
    except ValueError:
        print('ERRO: Insira apenas números!')

    
    continuar = input('Quer continuar? [S/N]: ').strip().upper()
    if continuar in ['N', 'NÃO', 'NAO']:
        break
    elif continuar not in ['S', 'SIM']:
        print('Digite apenas entre [S/N]')

    
print('Resultados...')
for nome, preco in cliente1.lista:
    print(f'{nome} - R${preco:.2f}')


print(cliente1.mostrar_total())
      
class Estoque:
    def __init__(self):
        self.lista = ['Mouse', 'Teclado', 'Monitor']

    
    def add_produto(self, produto):
        return self.lista.append(produto)
    
    def remover_produto(self, produto):
        if produto in self.lista:
            return self.lista.remove(produto)
        else:
            return f'ERRO: Produto: {produto} não está na lista!'
    
    def listar_itens(self):
        for i, produto in enumerate(self.lista):
            print(f'{i + 1}: {produto}')
        

estoque1 = Estoque()
estoque1.add_produto('Celular')
estoque1.remover_produto('Mouse')
estoque1.listar_itens()
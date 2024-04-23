#Samara Araujo e Alana Soares
class Produto:
    def __init__(self, nome, preço, quantidade_em_estoque):
        self.nome = nome
        self.preço = preço
        self.quantidade_em_estoque = quantidade_em_estoque

    def atualizar(self): 
         return f'O estoque é {self.quantidade_em_estoque} peças'

    def calcular(self): 
         return f'O preço total é {self.quantidade_em_estoque * self.preço} reais'

if __name__ == "__main__":
    produto1 = Produto("short", 90, 15)
    print(produto1.atualizar())
    print(produto1.calcular())


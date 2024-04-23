#Samara Araujo e Alana Soares
class Pessoa: 
    def __init__ (self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura 

    def informacoes (self): 
        return f'{self.nome}, {self.idade}, {self.altura}, são as informações de {self.nome}'
    def cumprimentar (self): 
        return f'{self.nome} está cumprimentando alguém: Oie, como vai?'

if __name__ == "__main__":
     pessoa1= Pessoa ("Alana", "17 anos", "1,63")
     print(pessoa1.informacoes())
     print(pessoa1.cumprimentar())
class Pessoa:
    def __init__(self, altura, idade):
        self.altura = altura
        self.idade = idade
        print(f"A pessoa tem {self.altura}m de altura e {self.idade} anos")

    def correr(self):
        print(f'Estou correndo')
    
    def comer(self):
        print(f'Estou comendo')

pessoa = Pessoa(1.66, 23)

pessoa.correr()
pessoa.comer()

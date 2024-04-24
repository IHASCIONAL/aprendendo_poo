class MinhaClasse:
    def __init__(self, info, elem):  # método construtor
        self.atributo_1 = "meu atributo"
        self.atributo_2 = elem
        self.atributo_3 = [1, 2, "a"]
        self.new_atribute = info
        print(self.new_atribute)

    def metodo_1(self):
        print("minha acao1")
        print("minha_acao2")
        print(self.atributo_2)
        return "Ola Mundo"
    
    def metodo_2(self, numero):
        print(self.atributo_3[1] + numero)


# objeto        #classe -> instanciamos um objeto
minha_classe = MinhaClasse("info aqui no construtor", 213)

response = minha_classe.metodo_1()
print(response)
minha_classe.metodo_2(3)

class MinhaClasse:
    def __init__(self) -> None:
        self.__valor = None
        self.__elem = None
    
    def setter_valor(self, valor: int) -> None:
        self.__valor = valor
    
    def setter_elem(self, elem: str) -> None:
        self.__elem = elem

    def getter_valor(self) -> int:
        return self.__valor
    
    def getter_elem(self) -> str:
        return self.__elem

my_class = MinhaClasse()

my_class.setter_valor(42)
valor = my_class.getter_valor()
print(valor)
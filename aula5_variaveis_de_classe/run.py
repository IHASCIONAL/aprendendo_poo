class MinhaClasse:

    estatico = "lhama"
    def __init__(self, estado) -> None:
        self.estado = estado


obj1 = MinhaClasse(True)
obj2 = MinhaClasse(True)

obj1.estatico = "Teste"

print(obj1.estatico)
print(obj2.estatico)
print(MinhaClasse.estatico)
# SOLID
# S - SINGLE RESPONSABILITY
# UM MÓDULO DEVE TER UM, E APENAS UM, MOTIVO PARA ALTERAÇÃO.

class SistemaCadastral:
    def cadastrar(self, nome: str, idade: int) -> None:
        if isinstance(nome, str) and isinstance(idade, int):
            print("Acessando o banco de dados...")
            print(f"Cadastrar usuario {nome}, idade {idade}")
        else:
            print("Dados inválidos!")
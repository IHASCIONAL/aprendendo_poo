class Loja:

    taxa:float = 1.0
    def __init__(self, valor_produto: float) -> None:
        self.valor_produto = valor_produto

    def consultar_valor_do_produto(self) -> float:
        print(self.valor_produto * self.taxa)

    @classmethod
    def editar_taxa_do_produto(cls, nova_taxa) -> float:
        cls.taxa = nova_taxa


loja_praia = Loja(30.50)
loja_shopping = Loja(10.39)
loja_rua = Loja(20.33)

loja_praia.consultar_valor_do_produto()
loja_shopping.consultar_valor_do_produto()
loja_rua.consultar_valor_do_produto()


loja_praia.editar_taxa_do_produto(1.35)

loja_praia.consultar_valor_do_produto()
loja_shopping.consultar_valor_do_produto()
loja_rua.consultar_valor_do_produto()
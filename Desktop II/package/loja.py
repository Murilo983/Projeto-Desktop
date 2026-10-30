from package.inventario import *
from rich import print
from rich import box
from rich.table import Table
from rich.panel import Panel

class Loja:
    @staticmethod
    def abrir_loja(heroi):
        while True:
            print(Panel.fit(f"Seu ouro: ${heroi.ouro:.1f}", title="BEM-VINDO À LOJA!", highlight=True))

            tabela_loja = Table(title = "\nInventário", box = box.HEAVY_EDGE)
            tabela_loja.add_column("Seleção")
            tabela_loja.add_column("Item")
            tabela_loja.add_column("Preço")
            tabela_loja.add_column("Descrição")
            for num, item in enumerate(itens, 1):
                tabela_loja.add_row(f"{num}", f"{item.nome}", f"{item.preco}",f"{item.descricao}")
            print(tabela_loja)
            print("[black on white] 0 - Voltar[/]")

            try:
                opcao = int(input("Escolha o item que deseja comprar: ") or 0)
            except ValueError:
                continue

            item_comprar = None
            preco = 0.0

            if opcao == 0:
                print("\nVolte sempre!")
                break
            elif opcao == 1:
                item_comprar = PocaoCura()
                preco = 20.0
            elif opcao == 2:
                item_comprar = Bomba()
                preco = 25.0
            else:
                continue

            if heroi.ouro >= preco:
                heroi.ouro -= preco
                heroi.inventario.adicionar_item(item_comprar)
                print(f"\nVocê comprou {item_comprar.nome}.")
            else:
                print("\nOuro insuficiente.")

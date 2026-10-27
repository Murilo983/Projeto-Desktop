from package.inventario import PocaoCura, Bomba

class Loja:
    @staticmethod
    def abrir_loja(heroi):
        while True:
            print(f"""\n==========================================
BEM-VINDO À LOJA!
Seu Ouro: ${heroi.ouro:.1f}
==========================================
1 - Comprar Poção de Cura (Preço: $20) - Restaura 15 pontos de vida
2 - Comprar Bomba (Preço: $25) - Causa 45 de dano fixo
0 - Sair da Loja""")

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

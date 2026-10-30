import time
from package.herois import Personagem
from package.inimigo import *
from rich import print
from rich import box
from rich.panel import Panel
from rich.table import Table

class Batalha:
    @staticmethod
    def iniciar_combate(heroi, inimigo):
        if heroi.esta_vivo and inimigo.esta_vivo:
            print("\n", Panel.fit(f"[red]{inimigo.nome.upper()} APARECEU! BATALHE![/]", style="blink", border_style="red"))
        else:
            print("\nNão há inimigo(s) para batalha.")

        while heroi.esta_vivo and inimigo.esta_vivo:
            while True:
                print("\n", Panel.fit(f"""HP de [blue]{heroi.nome}[/]: [green]{heroi.vida:.1f}[/] | HP de [magenta]{inimigo.nome}[/]: [green]{inimigo.vida:.1f}[/]
1 - Atacar
2 - Ver Status
3 - Usar item
4 - Fugir da batalha""", title="Turno do Jogador", highlight=True))
                try:
                    opcao = int(input("Escolha uma ação: ") or 1)
                    break
                except ValueError:
                    continue

            match opcao:
                case 1:
                    heroi.atacar(inimigo)

                    if not inimigo.esta_vivo:
                        print(f"\n{inimigo.nome} foi derrotado com sucesso.")
                        return "Vitória"

                    time.sleep(1)
                    print("\n", Panel.fit(f'[magenta]{inimigo.nome}[/] agiu!',title="Turno do Inimigo"))
                    inimigo.agir(heroi)

                    if not heroi.esta_vivo:
                        print(f"\n{heroi.nome} foi derrotado... Fim de jogo.")
                        heroi.vida = 1
                        return "Derrota"

                case 2:
                    tabela_status = Table(title=f"\nStatus de {heroi.nome}", box = box.HEAVY_EDGE, show_header=False)
                    tabela_status.add_row(f"Atq: {heroi.ataque}", f"Def: {heroi.defesa}")
                    tabela_status.add_row(f"Magia: {heroi.magia}", f"Resistência: {heroi.resistencia}")
                    print(tabela_status)

                case 3:
                    while True:
                        itens = heroi.inventario.obter_itens()
                        if not itens:
                            print("\nSeu inventário está vazio.")
                            break

                        tabela_inventario = Table(title = "\nInventário", box = box.HEAVY_EDGE)
                        tabela_inventario.add_column("Seleção")
                        tabela_inventario.add_column("Item")
                        tabela_inventario.add_column("Descrição")
                        for num, item in enumerate(itens, 1):
                            tabela_inventario.add_row(f"{num}", f"{item.nome}", f"{item.descricao}")
                        print(tabela_inventario)
                        print("[black on white] 0 - Voltar[/]")

                        try:
                            opcao = int(input("Escolha o item: ") or 0)
                            if opcao == 0:
                                break
                            if 1 <= opcao <= len(itens):
                                item_selecionado = itens[opcao - 1]

                                item_selecionado.usar_item(heroi, alvo=inimigo)
                                heroi.inventario.remover_item(item_selecionado)

                                if not inimigo.esta_vivo:
                                    print(f"\n{inimigo.nome} foi derrotado com sucesso.")
                                    return "Vitória"

                                time.sleep(1)
                                print("\n", Panel.fit(f'{inimigo.nome} agiu!',title="Turno do Inimigo"))
                                inimigo.agir(heroi)

                                if not heroi.esta_vivo:
                                    print(f"\n{heroi.nome} foi derrotado... Fim de jogo.")
                                    heroi.vida = 1
                                    return "Derrota"
                                break
                            else:
                                continue
                        except ValueError:
                            continue

                case 4:
                    print(f"\n{heroi.nome} fugiu da batalha.")
                    return 'Fugiu'

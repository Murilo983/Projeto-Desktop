import time
from package.herois import Personagem
from package.inimigo import *

class Batalha:
    @staticmethod
    def iniciar_combate(heroi, inimigo):
        if heroi.esta_vivo and inimigo.esta_vivo:
            print(f"\n==========================================")
            print(f"{inimigo.nome.upper()} APARECEU! BATALHE!")
            print(f"==========================================")
        else:
            print("\nNão há inimigo(s) para batalha.")

        while heroi.esta_vivo and inimigo.esta_vivo:
            while True:
                print(f"""\n--- Turno do Jogador ---
HP de {heroi.nome}: {heroi.vida:.1f} | HP de {inimigo.nome}: {inimigo.vida:.1f}
1 - Atacar
2 - Ver Status & Inventário
3 - Usar item
4 - Fugir da batalha""")
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
                    print(f"\n--- Turno do Inimigo ---")
                    inimigo.agir(heroi)

                    if not heroi.esta_vivo:
                        print(f"\n{heroi.nome} foi derrotado... Fim de jogo.")
                        heroi.vida = 1
                        return "Derrota"

                case 2:
                    print(f"\nStatus de {heroi.nome}:")
                    print(f"- Atq: {heroi.ataque} | Def: {heroi.defesa}")
                    print(f"- Atq Mágico: {heroi.magia} | Def Mágica: {heroi.resistencia}")
                    print(f"- Ouro: ${heroi.ouro}")
                    print(f"- Inventário: {heroi.inventario.listar_itens()}")

                case 3:
                    while True:
                        itens = heroi.inventario.obter_itens()
                        if not itens:
                            print("\nSeu inventário está vazio.")
                            continue

                        print(f"\n--- INVENTÁRIO ---")
                        for num, item in enumerate(itens, 1):
                            print(f"{num} - {item.nome} ({item.descricao})")
                        print("0 - Voltar")

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
                                print(f"\n--- Turno do Inimigo ---")
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

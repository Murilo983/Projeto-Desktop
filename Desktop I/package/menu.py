from package.herois import *
from package.batalha import *
from package.loja import Loja
import random

class Menu:
    @staticmethod
    def menu_principal(heroi):

        while True:
            print('''\nSeja Bem-Vindo ao lobby principal!
1 - Batalhar
2 - Loja
3 - Descansar
4 - Sair do jogo''')
            try:
                opcao = int(input("Opção: ") or 1)
                if 1<=opcao<=3:
                    pass
            except ValueError:
                continue

            match opcao:
                case 1:
                    while True:
                        print("\nSelecione um oponente para lutar: ")
                        for num, inimigo in enumerate(inimigos_lista, 1):
                            print(f"{num} - {inimigo.nome}")

                        try:
                            opcao = int(input("Opção: ") or 1)
                            if 1 <= opcao <= len(inimigos_lista):
                                break
                        except ValueError:
                            pass
                    inimigo = inimigos_lista[opcao-1]
                    resultado = Batalha.iniciar_combate(heroi, inimigo)

                    if resultado == "Vitória":
                        recompensa = random.randint(1, 15)
                        heroi.ouro += recompensa
                        print(f'Você recebeu {recompensa} de ouro.')

                case 2:
                    Loja.abrir_loja(heroi)
                case 3:
                    print("\nVocê decidiu descansar pelo resto do dia...")

                    heroi.restaurar_vida_completa()

                    for inimigo in inimigos_lista:
                        inimigo.restaurar_vida_completa()

                    time.sleep(1)
                    print(f"""Vida de {heroi.nome} foi totalmente restaurada ({heroi.vida:.1f}/{heroi._vida_maxima:.1f}).
Inimigos já derrotados reapareceram.""")
                case 4:
                    msg = "Finalizando..."
                    for x in msg:
                        print(x, end='')
                        time.sleep(0.1)
                    exit()

from package.herois import *
from package.inventario import *
from rich import print
from rich.panel import Panel

class Criacao():
    @staticmethod
    def criar_personagem():
        nome = str(input("Escolha o nome do seu personagem (máx. 12 caracteres): "))[:12] or "Flynn"
        while True:
            try:
                print("\n", Panel.fit("1 - Espadachim\n2 - Mago\n3 - Arqueiro", title="Escolha sua classe", highlight=True))
                classe_escolhida = int(input("Opção: ") or 1)
                if 0 < classe_escolhida < 4:
                    break
            except ValueError:
                continue

        match classe_escolhida:
            case 1:
                heroi = Espadachim(nome)
            case 2:
                heroi = Mago(nome)
            case 3:
                heroi = Arqueiro(nome)
        heroi.inventario.adicionar_item(PocaoCura())
        heroi.inventario.adicionar_item(Bomba())
        return heroi

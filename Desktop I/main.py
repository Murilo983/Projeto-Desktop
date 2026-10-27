from package.inventario import Item
from package.menu import Menu
from package.criacao import Criacao

def main():
    print(20*'=-=')
    print(25*' ' + 'RPG POO')
    print(20*'=-=')
    heroi = Criacao.criar_personagem()
    Menu.menu_principal(heroi)

if __name__ == "__main__":
    main()

from rich.table import Table
from abc import ABC, abstractmethod

class Item(ABC):
    def __init__(self, nome, descricao, preco):
        self._nome = nome
        self._descricao = descricao
        self._preco = preco

    @property
    def nome(self):
        return self._nome

    @property
    def descricao(self):
        return self._descricao

    @property
    def preco(self):
        return self._preco

    @abstractmethod
    def usar_item(self, usuario, alvo = None):
        pass

class PocaoCura(Item):
    def __init__(self, cura=15.0):
        super().__init__("Poção de Cura", "Restaura 15 pontos de vida.", 20)
        self.cura = cura

    def usar_item(self, usuario, alvo = None):
        vida_aux = usuario._vida
        usuario._vida += self.cura
        if usuario._vida > usuario._vida_maxima:
            self.cura = abs(usuario._vida_maxima - vida_aux)
            usuario._vida = usuario._vida_maxima
        print(f"\n{usuario.nome} usou {self.nome} e recuperou {self.cura} de HP.")

class Bomba(Item):
    def __init__(self, dano=45.0):
        super().__init__("Bomba", "Possui 45 de dano físico base.", 25)
        self.dano = dano

    def usar_item(self, usuario, alvo=None):
        print(f"\n{usuario.nome} lançou uma {self.nome} em {alvo.nome}.")
        alvo.receber_dano(self.dano, e_magico=False)
        return True

class Inventario:
    def __init__(self):
        self._itens = []

    def adicionar_item(self, item):
        self._itens.append(item)
        print(f"{item.nome} adicionado ao inventário.")

    def obter_itens(self):
        return self._itens

    def remover_item(self, item):
        if item in self._itens:
            self._itens.remove(item)
itens = [PocaoCura(), Bomba()]

from abc import ABC, abstractmethod
from package.inventario import Inventario

class Personagem(ABC):
    def __init__(self, nome, vida, ataque, defesa, magia, resistencia):
        self._nome = nome
        self._vida_maxima = vida
        self._vida = vida
        self._ataque = ataque
        self._defesa = defesa
        self._magia = magia
        self._resistencia = resistencia
        self._inventario = Inventario()
        self._ouro = 50.0

    @property
    def nome(self):
        return self._nome

    @property
    def vida(self):
        return self._vida

    @vida.setter
    def vida(self, valor):
        self._vida = max(0.0, min(valor, self._vida_maxima))

    @property
    def ataque(self):
        return self._ataque

    @ataque.setter
    def ataque(self, valor):
        self._ataque = max(0.0, float(valor))

    @property
    def defesa(self):
        return self._defesa

    @property
    def magia(self):
        return self._magia

    @magia.setter
    def magia(self, valor):
        self._magia = max(0.0, float(valor))

    @property
    def resistencia(self):
        return self._resistencia

    @property
    def inventario(self):
        return self._inventario

    @property
    def esta_vivo(self):
        return self._vida > 0

    @property
    def ouro(self):
        return self._ouro

    @ouro.setter
    def ouro(self, valor):
        self._ouro = max(0.0, float(valor))

    @abstractmethod
    def atacar(self, alvo):
        pass

    def receber_dano(self, dano_bruto, e_magico = False):
        defesa_usada = self._resistencia if e_magico else self._defesa
        dano_final = max(1.0, dano_bruto - defesa_usada)
        self.vida -= dano_final
        print(f"{self._nome} recebeu {dano_final:.1f} de dano! (Vida restante: {self.vida:.1f}/{self._vida_maxima})")

    def restaurar_vida_completa(self):
        self.vida = self._vida_maxima

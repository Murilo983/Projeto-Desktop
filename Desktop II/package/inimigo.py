import random
from package.personagem import Personagem

class Inimigo(Personagem):
    def __init__(self, nome, vida, ataque, defesa, magia, resistencia):
        super().__init__(nome, vida, ataque, defesa, magia, resistencia)

    def atacar(self, alvo):
        print(f"{self.nome} ataca {alvo.nome}.")
        if self.ataque > self.magia:
            alvo.receber_dano(self.ataque, e_magico=False)
        else:
            alvo.receber_dano(self.magia, e_magico=True)

    def regenerar_inimigo(self):
        cura = self.vida * 0.25 + 5
        self.vida += cura
        print(f"{self.nome} curou {cura:.1f} pontos de vida.")

    def desesperar(self, alvo):
        if self.ataque > self.magia:
            status_aux = self.ataque
            self.ataque *= 1.5
            alvo.receber_dano(self.ataque, e_magico=False)
            self.ataque = status_aux
        else:
            status_aux = self.magia
            self.magia *= 1.5
            alvo.receber_dano(self.magia, e_magico=True)
            self.magia = status_aux

    def agir(self, alvo):
        if self.vida <= 0.75*self._vida_maxima:
            escolha = random.choice(["ataque", "regenerar", "desespero"])
        else:
            escolha = "ataque"
        if escolha == "ataque":
            self.atacar(alvo)
        elif escolha == "regenerar":
            self.regenerar_inimigo()
        else:
            self.desesperar(alvo)

#Inimigos
goblin = Inimigo("Goblin da Floresta", vida = 75.0, ataque = 19.0, defesa = 12.0, magia = 8.0, resistencia = 6.0)
fantasma = Inimigo("Fantasma Vingativo", vida = 70.0, ataque = 14.0, defesa = 25.0, magia = 18.0, resistencia = 16.0)
rato = Inimigo("Rato GIGANTE", vida = 90.0, ataque = 22.0, defesa = 10.0, magia = 5.0, resistencia = 8.0)
inimigos_lista = [goblin, fantasma, rato]

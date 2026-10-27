from package.personagem import Personagem

class Espadachim(Personagem):
    def __init__(self, nome):
        super().__init__(nome, vida = 100.0, ataque = 25.0, defesa = 12.0, magia = 0.0, resistencia = 3.0)

    def atacar(self, alvo):
        print(f"\n{self.nome} ataca {alvo.nome}.")
        alvo.receber_dano(self.ataque, e_magico = False)

class Mago(Personagem):
    def __init__(self, nome,):
        super().__init__(nome, vida = 80.0, ataque = 8.0, defesa = 4.0, magia = 30.0, resistencia = 18.0)

    def atacar(self, alvo):
        print(f"\n{self.nome} ataca {alvo.nome}.")
        alvo.receber_dano(self.magia, e_magico=True)

class Arqueiro(Personagem):
    def __init__(self, nome):
        super().__init__(nome, vida = 90.0, ataque = 18.0, defesa = 11.0, magia = 10.0, resistencia = 11.0)

    def atacar(self, alvo):
        print(f"\n{self.nome} ataca {alvo.nome}.")
        alvo.receber_dano(self.ataque, e_magico=False)

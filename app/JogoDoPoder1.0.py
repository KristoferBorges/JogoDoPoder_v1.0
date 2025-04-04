class Jogador:
    def __init__(self):
        self.name = ""
        self.level = 1
        self.power = 0


class Monstro:
    def __init__(self):
        self.name = ""
        self.level = 1
        self.power = 0
        

class Batalha:
    def __init__(self, jogador, monstro):
        self.jogador = jogador
        self.monstro = monstro

    def iniciar_batalha(self):
        print(f"Começou a batalha entre {self.jogador.name} e {self.monstro.name}!")
        if self.jogador.power > self.monstro.power:
            print(f"{self.jogador.name} venceu a batalha!")
        elif self.jogador.power < self.monstro.power:
            print(f"{self.monstro.name} venceu a batalha!")
        else:
            print(f"{self.monstro.name} venceu a batalha!")
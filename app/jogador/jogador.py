from random import randint
from time import sleep
class Jogador:
    """
    Classe Jogador que representa um jogador no jogo.
    
    Atributos:
        name (str): Nome do jogador.
        level (int): Nível do jogador.
        power (float): Poder do jogador.
        apostado (float): Valor apostado pelo jogador.
    
    Métodos:
        habilidadePoderExtra(): Habilidade de aumentar o poder do jogador.
        habilidadePularBoss(): Habilidade de pular um boss.
    """
    def __init__(self):
        self.name: str= "Jogador 1"
        self.level: int = 1
        self.power: float = randint(1000, 4000)
        self.habilidade: str = None
        self.qntHabilidadePoderExtra: int = 3
        self.qntHabilidadePularBoss: int = 1
        self.apostado: float = 0
        self.aumentoDePoder: int = 0
    
    def habilidadePoderExtra(self):
        """
        Habilidade de aumentar o poder do jogador.
        """
        if self.habilidade == "Aumento de Poder":
            chanceDeUso = randint(1, 20)
            self.aumentoDePoder = randint(100, 2000)
            if chanceDeUso == 1 and self.qntHabilidadePoderExtra > 0:
                self.qntHabilidadePoderExtra = self.qntHabilidadePoderExtra - 1
                self.power = self.power + self.aumentoDePoder

                return True
            else:
                return False
    def habilidadePularBoss(self, nomeMonstro: str):
        """
        Habilidade de pular um boss.
        """
        if nomeMonstro == "Boss Infernal" and self.habilidade == "Pular Boss":
            pass
            
            
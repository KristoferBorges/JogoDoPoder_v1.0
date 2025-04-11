from random import randint
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
        self.power: float = randint(1000, 5000)
        self.apostado: float = 0
    
    def habilidadePoderExtra(self):
        """
        Habilidade de aumentar o poder do jogador.
        """
        pass
    
    def habilidadePularBoss(self):
        """
        Habilidade de pular um boss.
        """
        pass
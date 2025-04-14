from random import randint
class Monstro:
    def __init__(self):
        self.name: str = ""
        self.level: int = 1
        self.power: float = None
        self.chanceDeAparicao: int = randint(1, 20)
        
    def bossInfernal(self):
        """
        Função para gerar o Boss Infernal durante o jogo.
        """
        if self.chanceDeAparicao == 1:
            self.name = "Boss Infernal"
            self.level = randint(70, 100)
            self.power = (self.level * 10) + randint(500, 20000)
            
            return True
        return False
        
            
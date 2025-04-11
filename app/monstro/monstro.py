from random import randint
class Monstro:
    def __init__(self):
        self.name = ""
        self.level = 1
        self.power = None
        self.chanceDeAparicao = randint(1, 7)
        
    def bossInfernal(self):
        """
        Função para gerar o Boss Infernal durante o jogo.
        """
        if self.chanceDeAparicao == 1:
            self.name = "Boss Infernal"
            self.level = randint(70, 100)
            self.power = (self.level * 10) + randint(500, 7000)
            
            return True
        return False
        
            
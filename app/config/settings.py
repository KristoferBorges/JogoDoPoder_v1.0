import os

class Settings:
    def __init__(self):
        self.vantagemMaster = False
        self.valorMinimo = 10000
        self.teste = True
        self.caminhoGameData = "config/gameData.yaml"
        self.aumentoDePoder = 410
        self.quantidadeDeJogos = 1
        self.velocidadeDoJogo = 0.1
        self.velocidadeDoJogoBoss = 0.5
        self.danoAoJogador = 30
        self.danoAoMonstro = 30
        self.danoRefletidoAoMonstro = 40
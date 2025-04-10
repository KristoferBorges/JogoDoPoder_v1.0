import os

class Settings:
    def __init__(self):
        self.vantagemMaster = False # Variável para definir a vantagem do jogo (Alteração manual para garantir mais ganhos)
        self.teste = True # Variável para definir o testes rápidos sem o menu
        self.caminhoGameData = "config/gameData.yaml"
        self.aumentoDePoder = 312 # Aumento de poder do jogador para cada vitória
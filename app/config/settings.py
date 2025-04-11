import os

class Settings:
    def __init__(self):
        self.vantagemMaster = False # Variável para definir a vantagem do jogo (Alteração manual para garantir mais ganhos)
        self.valorMinimo = 10000 # Valor mínimo definido para que a banca comece a ter vantagem (Desativado se vantagemMaster = False)
        self.teste = True # Variável para definir o testes rápidos sem o menu
        self.caminhoGameData = "config/gameData.yaml"
        self.aumentoDePoder = 312 # Aumento de poder do jogador para cada vitória
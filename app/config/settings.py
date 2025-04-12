class Settings:
    def __init__(self):
        self.vantagemMaster: bool = False
        self.valorMinimo: int = 10000
        self.teste: bool = True
        self.skip: bool = False
        self.caminhoGameData: str = "config/gameData.yaml"
        self.aumentoDePoder: int = 410
        self.quantidadeDeJogos: int = 10
        self.velocidadeDoJogo: float = 0.0
        self.velocidadeDoJogoBoss: float = 0.0
        self.danoAoJogador: int = 30
        self.danoAoMonstro: int = 30
        self.danoRefletidoAoMonstro: int = 40
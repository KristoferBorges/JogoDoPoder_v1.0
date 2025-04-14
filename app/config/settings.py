class Settings:
    def __init__(self):
        self.vantagemMaster: bool = False
        self.valorMinimo: int = 10000
        self.teste: bool = True
        self.skip: bool = False
        self.habilidadeTeste: str = "Pular Boss" # Aumento de Poder | Pular Boss | Nenhuma habilidade
        self.caminhoGameData: str = "config/gameData.yaml"
        self.aumentoDePoder: int = 380.13
        self.quantidadeDeJogos: int = 100
        self.velocidadeDoJogo: float = 0.0
        self.velocidadeDoJogoBoss: float = 0.0
        self.velocidadeAumentoDePoder: float = 0.0
        self.danoAoJogador: int = 30
        self.danoAoMonstro: int = 30
        self.danoRefletidoAoMonstro: int = 40
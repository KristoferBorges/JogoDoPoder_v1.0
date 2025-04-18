import yaml
from jogador.jogador import Jogador
from monstro.monstro import Monstro
from config.settings import Settings
from batalha.batalha import Batalha

if __name__ == "__main__":
    try:
        settings = Settings()
        for i in range(settings.quantidadeDeJogos): # Jogos em sequência
            # Coleta os dados do arquivo gameData.yaml
            with open(settings.caminhoGameData, 'r', encoding='utf-8') as arquivo:
                dados = yaml.safe_load(arquivo)
                if not isinstance(dados, dict):
                    raise ValueError("O arquivo YAML não contém um dicionário válido.")
            
            jogador = Jogador()
            monstro = Monstro()
            batalha = Batalha(jogador, monstro, dados)
            batalha.menu()
            batalha.escolhaDeMonstro(batalha.plataformaComVantagem)
            batalha.iniciar_batalha()
    
    except Exception as e:
        print(f"Erro no main.py, carregamento comprometido - {e}")
        exit(1)
import yaml
import os
import random

# Caminho relativo: volta uma pasta e entra em 'config/settings.yaml'
caminho_arquivo = os.path.join('..', 'config', 'settings.yaml')

with open(caminho_arquivo, 'r', encoding='utf-8') as f:
    dados = yaml.safe_load(f)

monstros = dados['monstros']
monstro_sorteado = random.choice(list(monstros.keys()))
print(monstro_sorteado)
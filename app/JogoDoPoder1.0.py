import random
import yaml
import os
import pdb
from time import sleep
from jogador.jogador import Jogador
from monstro.monstro import Monstro
from config.settings import Settings

# Cores
red = '\033[31m'
green = '\033[32m'
yellow = '\033[33m'
ciano = '\033[36m'
normal = '\033[m'

class Batalha:
    def __init__(self, jogador, monstro):
        self.jogador = jogador
        self.monstro = monstro
        self.continuar = True
        self.plataformaComVantagem = Batalha.definirVantagem(self)
    
    def menu(self):
        # Tela inicial
        print('\n\n\n\n')
        print(yellow + '{:¨^41}'.format('¨'))
        print('{:¨^41}'.format('| Bem-vindo |'))
        print('{:¨^41}'.format('| Ao |'))
        print('{:¨^41}'.format('| JOGO DO PODER |'))
        print('{:¨^41}'.format('¨'))
        print('{:-^41}'.format('-'))
        print('\n\n')
        print('{:^41}'.format('Deseja entrar na Dungeon do Boss?'))
        print(green + '                 Sim' + yellow + ' / ' + red + 'Não              ' + normal)
        
        # Checando variável de teste
        if settings.teste == True:
            iniciar_jogo = 'SIM'
        else:
            iniciar_jogo = str(input('    --> ')).upper().strip()
            
        if iniciar_jogo == 'SIM' or iniciar_jogo == 'S':
            # Inserção de Dinheiro
            print(yellow + '    MAX - R$ 100,00' + normal)
            print(green + '    Qual valor deseja apostar?')
            
            # Checando variável de teste
            if settings.teste == True:
                self.apostado = 100
            else:
                self.apostado = float(input('    R$' + normal))
            print('\n')

            Batalha.iniciar_batalha(self)
            
    def iniciar_batalha(self):
        
        while self.continuar == True:
            # sleep(0.1)	
            # Informação na tela
            print(green + f'   {jogador.name}', end=' ')
            print(yellow + f'Lv {jogador.level}' + normal + ' X ' + red + f'{monstro.name}', end=' ')
            print(yellow + f'Lv {monstro.level}')
            print(f'   Power: {jogador.power:.2f}' + normal, end='   X')
            print(yellow + f'   Power: {monstro.power:.2f}' + normal)

            # Resultado do round
            if jogador.power > monstro.power:
                print(green + '  -x-x-x-x- Usuário Win -x-x-x-x-' + normal + '\n')
                Batalha.sofrimentoDeDano(self, 'monstro')
                
            elif jogador.power < monstro.power:
                print(red + '  -x-x-x-x- Monstro Win -x-x-x-x-' + normal + '\n')
                Batalha.sofrimentoDeDano(self, 'jogador')
                
            else:
                print(ciano + '  -x-x-x-x- Empate -x-x-x-x-' + normal + '\n')
                Batalha.sofrimentoDeDano(self, 'ambos')

    
    def sofrimentoDeDano(self, alvo):
        if alvo == 'monstro':
            # Dano no monstro
            self.monstro.power -= (jogador.power / 30)
            self.jogador.power += settings.aumentoDePoder
            self.jogador.level += 1
            
            if self.monstro.power <= 0:
                print(f'O {self.monstro.name} foi derrotado!')
                Batalha.escolhaDeMonstro(self, self.plataformaComVantagem)
                
        elif alvo == 'jogador':
            # Dano no jogador
            self.jogador.power -= (monstro.power / 30)
            # Refletindo o dano no monstro
            self.monstro.power -= (monstro.power / 100)
            
            if self.jogador.power <= 0:
                print(f'O {self.jogador.name} foi derrotado!')
                Batalha.abatimentoNoDinheiro(self, 'derrota')
        else:
            # Empate
            self.jogador.power -= (monstro.power / 20)
            self.monstro.power -= (jogador.power / 20)
            if self.jogador.power <= 0:
                print(f'O {self.jogador.name} foi derrotado!')
            elif self.monstro.power <= 0:
                print(f'O {self.monstro.name} foi derrotado!')
            elif self.jogador.power <= 0 and self.monstro.power <= 0:
                print('Ambos os lados foram derrotados!')
                Batalha.abatimentoNoDinheiro(self, 'empate')
        
        if self.jogador.level >= 100:
            Batalha.abatimentoNoDinheiro(self, 'vitoria')
    
    def escolhaDeMonstro(self, plataformaComVantagem):
        jogador = Jogador() # Instância do jogador
        monstros = dados['monstros']
        
        if plataformaComVantagem == True:
            monstroEscolhido = random.choice(list(monstros.keys()))
            monstroPower = monstros[monstroEscolhido]
            self.monstro.name = monstroEscolhido
            self.monstro.power = monstroPower
            
            # Tenta garantir a vantagem com um monstro forte
            for _ in range(20):
                if monstroPower < jogador.power:
                    monstroEscolhido = random.choice(list(monstros.keys()))
                    monstroPower = monstros[monstroEscolhido]
                    self.monstro.name = monstroEscolhido
                    self.monstro.power = monstroPower
        
        else:
            monstroEscolhido = random.choice(list(monstros.keys()))
            monstroPower = monstros[monstroEscolhido]
            self.monstro.name = monstroEscolhido
            self.monstro.power = monstroPower

        return monstroEscolhido, monstroPower
    
    def definirVantagem(self):
        plataformaComVantagem = None # Variável para definir a vantagem do jogo
        
        if dados['banca']['dinheiro'] < 10000 and settings.vantagemMaster == True:
            if random.Random().randint(1, 6) >= 3:
                plataformaComVantagem = True               
            else:
                plataformaComVantagem = False
            
        return plataformaComVantagem

    def abatimentoNoDinheiro(self, resultado):
        if resultado == 'vitoria':
            dados['banca']['dinheiro'] -= self.apostado
        elif resultado == 'derrota':
            dados['banca']['dinheiro'] += self.apostado
        else:
            dados['banca']['dinheiro'] = dados['banca']['dinheiro'] # Valor padrão
        
        self.continuar = False
        
        # Atualiza o arquivo gameData.yaml
        with open(settings.caminhoGameData, 'w', encoding='utf-8') as arquivo:
            yaml.dump(dados, arquivo, default_flow_style=False, allow_unicode=True)

# Testa a escolha do monstro

if __name__ == "__main__":
    
    for i in range(10): # Jogos em sequência
        # Coleta os dados do arquivo gameData.yaml
        try:
            settings = Settings()
            
            with open(settings.caminhoGameData, 'r', encoding='utf-8') as arquivo:
                dados = yaml.safe_load(arquivo)
                if not isinstance(dados, dict):
                    raise ValueError("O arquivo YAML não contém um dicionário válido.")
        except Exception as e:
            print(f"Erro ao carregar o arquivo YAML: {e}")
            exit(1)
        
        jogador = Jogador()
        monstro = Monstro()
        batalha = Batalha(jogador, monstro)
        batalha.escolhaDeMonstro(batalha.plataformaComVantagem)
        batalha.menu()
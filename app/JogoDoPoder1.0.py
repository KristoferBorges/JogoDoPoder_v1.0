import random

banca = 1000 # Valor que a plataforma tem para jogar
vantagemMaster = False # Variável para definir a vantagem do jogo (Alteração manual para garantir mais ganhos)

# Cores
red = '\033[31m'
green = '\033[32m'
yellow = '\033[33m'
ciano = '\033[36m'
normal = '\033[m'

all_monsters = {
    # Monstros do Nível 1
    'Goblin': 150,
    'Rato': 50,
    'Esqueleto': 100,
    'Slime': 75,
    'Aranha': 80,
    'Zumbi': 140,
    'Duende': 90,

    # Monstros do Nível 2
    'Bandido': 160,
    'Orc': 350,
    'Mago': 400,
    'Fantasma': 300,
    'Arcano': 500,
    'Ogro': 400,
    'Escorpião': 310,
    'Cobra Selvagem': 260,
    'Lobo': 200,
    'Crocodilo': 240,

    # Monstros do Nível 3
    'Fada': 900,
    'Spectro': 1300,
    'Guerreiro Sombrio': 1400,
    'Clérigo Corrompido': 1450,

    # Monstros do Nível 4
    'Gigante': 3000,
    'Monstro do Lago': 3500,
    'Dragão': 4650,

    # Monstros Especiais (Alta Dificuldade)
    'Zumbi Gigante': 4700,
    'Leviatã': 4960,
    'Dragão Negro': 5500,
    'Fênix Dourada': 5600,
    'Troll Raivoso': 4680,
    'Basilisco': 4700,
    'Hidra': 5300,
    'Grifo': 4800,
    'Gólem': 5120
}

class Jogador:
    def __init__(self):
        self.name = "Jogador 1"
        self.level = 1
        self.power = 5000


class Monstro:
    def __init__(self):
        self.name = ""
        self.level = 1
        self.power = None
        

class Batalha:
    def __init__(self, jogador, monstro):
        self.jogador = jogador
        self.monstro = monstro
    
    def iniciar_batalha(self):
        # Informação na tela
        print(green + f'   {jogador.name}', end=' ')
        print(yellow + f'Lv {jogador.level}' + normal + ' X ' + red + f'{monstro.name}', end=' ')
        print(yellow + f'Lv {monstro.level}')
        print(f'   Power: {jogador.power}' + normal, end='   X')
        print(yellow + f'   Power: {monstro.power}' + normal)

        # Resultado do round
        if jogador.power > monstro.power:
            print(green + '  -x-x-x-x- Usuário Win -x-x-x-x-' + normal + '\n')

        
    def escolhaDeMonstro(self, plataformaComVantagem):
        jogador = Jogador() # Instância do jogador
        
        if plataformaComVantagem == True:
            monstroEscolhido = random.choice(list(all_monsters.keys()))
            monstroPower = all_monsters[monstroEscolhido]
            self.monstro.name = monstroEscolhido
            self.monstro.power = monstroPower
            
            # Garante a vantagem com um monstro forte
            while monstroPower < jogador.power:
                monstroEscolhido = random.choice(list(all_monsters.keys()))
                monstroPower = all_monsters[monstroEscolhido]
                self.monstro.name = monstroEscolhido
                self.monstro.power = monstroPower
            
        else:
            monstroEscolhido = random.choice(list(all_monsters.keys()))
            monstroPower = all_monsters[monstroEscolhido]
            self.monstro.name = monstroEscolhido
            self.monstro.power = monstroPower
        
        return monstroEscolhido, monstroPower
    
    def definirVantagem(self):
        plataformaComVantagem = None # Variável para definir a vantagem do jogo
        
        if banca < 2000 or vantagemMaster == True:
            if random.Random().randint(1, 6) >= 3:
                plataformaComVantagem = True               
            else:
                plataformaComVantagem = False
            
        return plataformaComVantagem


# Testa a escolha do monstro

jogador = Jogador()
monstro = Monstro()
batalha = Batalha(jogador, monstro)
plataformaComVantagem = batalha.definirVantagem()
batalha.escolhaDeMonstro(plataformaComVantagem)
batalha.iniciar_batalha()
        

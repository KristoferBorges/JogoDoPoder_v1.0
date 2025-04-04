# import pdb
from pygame import mixer
import random
from time import sleep
from functions import utils

# Sons / Musicas
mixer.init()
selecionar = mixer.Sound(r'.\public\escolha12.wav')
lose = mixer.Sound(r'.\public\lose.wav')
win = mixer.Sound(r'.\public\winwin.wav')
boss = mixer.Sound(r'.\public\infernal2.wav')
bonus = mixer.Sound(r'.\public\bonus.wav')
critico = mixer.Sound(r'.\public\critico.wav')
roar1 = mixer.Sound(r'.\public\Roar1.mp3')
roar2 = mixer.Sound(r'.\public\Roar2.mp3')
roar3 = mixer.Sound(r'.\public\Roar3.mp3')
roar4 = mixer.Sound(r'.\public\Roar4.mp3')
roarlose = mixer.Sound(r'.\public\RoarLose.mp3')
roardead = mixer.Sound(r'.\public\Roardead.mp3')
mixer.music.load(r'.\public\digital.mp3')
mixer.music.play(-1)

# Dicionário com todos os monstros e seus poderes iniciais
all_monsters = {
    # Monstros do Nível 1
    'Goblin': 0,
    'Rato': 0,
    'Esqueleto': 0,
    'Slime': 0,
    'Aranha': 0,
    'Zumbi': 0,
    'Duende': 0,

    # Monstros do Nível 2
    'Bandido': 0,
    'Orc': 0,
    'Mago': 0,
    'Fantasma': 0,
    'Arcano': 0,
    'Ogro': 0,
    'Escorpião': 0,
    'Cobra Selvagem': 0,
    'Lobo': 0,
    'Crocodilo': 0,

    # Monstros do Nível 3
    'Fada': 0,
    'Spectro': 0,
    'Guerreiro Sombrio': 0,
    'Clérigo Corrompido': 0,

    # Monstros do Nível 4
    'Gigante': 0,
    'Monstro do Lago': 0,
    'Dragão': 0,

    # Monstros Especiais (Alta Dificuldade)
    'Zumbi Gigante': 0,
    'Leviatã': 0,
    'Dragão Negro': 0,
    'Fênix Dourada': 0,
    'Troll Raivoso': 0,
    'Basilisco': 0,
    'Hidra': 0,
    'Grifo': 0,
    'Gólem': 0
}

# Monstros do Nível 10 (Boss)
monsters_boss = {
    'Infernal': 0
}

card_monster = random.choice(list(all_monsters.keys()))

# Definição de power por nível do usuário
user_card = ['Guerreiro', 'Espadachim', 'Arqueiro', 'Cavaleiro', 'Arcanista']
usuario = random.choice(user_card)
user_level = random.randint(1, 4)

# Nível de poder de cada usuário
power_usuario = 1500
power_lv1 = 1530
power_lv2 = 2300
power_lv3 = 3440
power_lv4 = 5300

# Cores
red = '\033[31m'
green = '\033[32m'
yellow = '\033[33m'
ciano = '\033[36m'
normal = '\033[m'

# Variáveis importantes!
resultado = ''
escolha = ''
skipBoss = 0
choiceBonus = 0
escolha_usar_item = 0
soma_nivel = 0
aposta = 0
multiplicador = 0.00
lv_monster_print = 0
lv_choice = 0
roarChoice = 0
# pontos
point = 0
pointx = random.randint(1, 10)

# Contador de Batalhas
cont = 0

# Processo para elevação de poder / nível após certo nível //
def aumento_de_poder():
    global user_level, lv_monster, power_monster, lv_choice
    if user_level > 70 and power_usuario > 16000:
        lv_choice = random.randint(3, 7)
        lv_monster = lv_monster + lv_choice
        power_monster = power_monster * lv_choice


def roar():
    global roarChoice
    roarChoice = random.randint(1, 4)
    if roarChoice == 1:
        utils.Musics.roar1.play()
    elif roarChoice == 2:
        utils.Musics.roar2.play()
    elif roarChoice == 3:
        utils.Musics.roar3.play()
    elif roarChoice == 4:
        utils.Musics.roar4.play()


def critico_infernal():
    global power_usuario, point
    if random.randint(1, 7) == 1:
        utils.Musics.critico.play()
        print(red + '   INFERNAL USOU SUA ULTMATE E INFRINGIU 5000 DE DANO' + normal)
        print(red + '   -100 Pontos' + normal)
        power_usuario = power_usuario - 5000
        point = point - 100
        sleep(3)

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
iniciar_jogo = str(input('    --> ')).upper().strip()
if iniciar_jogo == 'SIM' or iniciar_jogo == 'S':
    # Music
    utils.Musics.selecionar.play()
    # Itens e BUFFS dentro do game
    print('\n')
    print(ciano + '{:^41}'.format('| Itens EXTRA |'))
    print('   Escolha| Descrição| Quantidade')
    print('     [1] - Skip de Boss (1)')
    print('     [2] - CHANCE DE GANHAR PODER EXTRA (2)' + normal)
    item_escolhido = int(input('     ---> '))
    utils.Musics.selecionar.play()

    if item_escolhido == 1:
        skipBoss = 1
        print(green + '    Você Escolheu (SKIP DE BOSS)!' + normal)
        print('\n')
    elif item_escolhido == 2:
        choiceBonus = 2
        print(green + '    Você Escolheu (BONUS DE PODER)!' + normal)
        print('\n')
    else:
        print(red + '    Nenhum item escolhido!' + normal)
        print('\n')

    # Inserção de Dinheiro
    print(yellow + '    MAX - R$ 100,00' + normal)
    print(green + '    Qual valor deseja apostar?')
    aposta = float(input('    R$' + normal))
    utils.Musics.selecionar.play()
    print('\n')

    # Função de vitória/derrota/empate
    def result():
        global power_monster, power_usuario, user_level, lv_monster, resultado, point, pointx, card_monster, escolha, \
            soma_nivel, valorTotal, aposta, multiplicador
        if power_usuario > power_monster:
            user_level = user_level + 1
            power_usuario = power_usuario + 413
            power_monster = 0
            print(green + '  -x-x-x-x- Usuário Win -x-x-x-x-' + normal)
            print('\n')
            resultado = 'win'
            if resultado == 'win':
                point = point + 10
                multiplicador = multiplicador + 0.01
                if card_monster == 'Infernal':
                    utils.Musics.roardead.play()
                if user_level >= 70:
                    card_monster = random.choice(monsters_high)
                else:
                    card_monster = random.choice(monsters)
                lv_monster = random.randint(1, 4)
        elif power_monster > power_usuario:
            # Redução de poder por batalha / Monstro Win
            if card_monster == 'Infernal':
                point = point - 10
                if power_monster > power_usuario and card_monster == 'Infernal':
                    # Rugido
                    roar()
            else:
                point = point - random.randint(3, 10)
            power_usuario = power_usuario - 250
            power_monster = power_monster - 450
            soma_nivel = soma_nivel + 1
            if soma_nivel == 2:
                lv_monster = lv_monster + 1
                soma_nivel = 0

            print(red + '  -x-x-x-x- Monstro Win -x-x-x-x-' + normal)
            print('\n')
            resultado = 'lose'
        elif power_usuario == power_monster:
            print('  -x-x-x-x- Empate -x-x-x-x-')
            print('\n')
            resultado = 'tied'
            power_monster = 0
            card_monster = random.choice(monsters)
            lv_monster = random.randint(1, 4)
            # Redução de poder por batalha / Empate
            power_usuario = power_usuario - 100
            power_monster = power_monster - 500

    if user_level == 1:
        power_usuario = power_usuario + power_lv1
    elif user_level == 2:
        power_usuario = power_usuario + power_lv2
    elif user_level == 3:
        power_usuario = power_usuario + power_lv3
    elif user_level == 4:
        power_usuario = power_usuario + power_lv4

    # Condicionais para V/D monstros
    while power_usuario > 0:
        # Variáveis para o Item de bonus
        powerBonus = random.randint(1000, 3000)
        choice = random.randint(1, 25)
        sleep(0.15)
        # Definição de níveis conforme a entidade + poder inicial
        if lv_monster == 1:
            power_monster = power_monster + power_lv1
            aumento_de_poder()
            if card_monster == 'Infernal':
                utils.Musics.boss.play()
                print(red + '   VOCÊ ENCONTROU UM BOSS INFERNAL NIVEL 10')
                if skipBoss >= 1:
                    print(green + '    Você possui um item para Fugir!')
                    print('    Deseja Fugir?')
                    print(green + '                 Sim' + yellow + ' / ' + red + 'Não              ' + normal)
                    escolha_usar_item = str(input('    --> ')).upper().strip()
                    if escolha_usar_item == 'SIM' or escolha_usar_item == 'S':
                        utils.Musics.selecionar.play()
                        print(ciano + '    Você Fugiu!')
                        print(ciano + '    Seu item foi Consumido!')
                        skipBoss = skipBoss - 1
                        card_monster = random.choice(monsters)
                        lv_monster = random.randint(1, 4)
                        sleep(1.5)
                    else:
                        utils.Musics.selecionar.play()
                        print(ciano + '    Você não usou o item!')
                        power_monster = power_monster + monster_power_lv10
                        lv_monster = 10
                        user_level = user_level - 5
                        power_usuario = power_usuario - 1000
                        print(red + '   DANO CRÍTICO!' + normal)
                        sleep(1.5)
                        critico_infernal()
                elif skipBoss <= 0:
                    power_monster = power_monster + monster_power_lv10
                    lv_monster = 10
                    user_level = user_level - 5
                    power_usuario = power_usuario - 1000
                    print(red + '   DANO CRÍTICO!' + normal)
                    sleep(1.5)
                    critico_infernal()
                print('\n')
        elif lv_monster == 2:
            power_monster = power_lv2
            aumento_de_poder()
            if card_monster == 'Infernal':
                utils.Musics.boss.play()
                print(red + '   VOCÊ ENCONTROU UM BOSS INFERNAL NIVEL 10')
                if skipBoss >= 1:
                    print(green + '    Você possui um item para Fugir!')
                    print('    Deseja Fugir?')
                    print(green + '                 Sim' + yellow + ' / ' + red + 'Não              ' + normal)
                    escolha_usar_item = str(input('    --> ')).upper().strip()
                    if escolha_usar_item == 'SIM' or escolha_usar_item == 'S':
                        utils.Musics.selecionar.play()
                        print(ciano + '    Você Fugiu!')
                        print(ciano + '    Seu item foi Consumido!')
                        skipBoss = skipBoss - 1
                        card_monster = random.choice(monsters)
                        lv_monster = random.randint(1, 4)
                        sleep(1.5)
                    else:
                        utils.Musics.selecionar.play()
                        print(ciano + '    Você não usou o item!')
                        power_monster = power_monster + monster_power_lv10
                        lv_monster = 10
                        user_level = user_level - 5
                        power_usuario = power_usuario - 1000
                        print(red + '   DANO CRÍTICO!' + normal)
                        sleep(1.5)
                        critico_infernal()
                elif skipBoss <= 0:
                    power_monster = power_monster + monster_power_lv10
                    lv_monster = 10
                    user_level = user_level - 5
                    power_usuario = power_usuario - 1000
                    point = point - 100
                    print(red + '   DANO CRÍTICO!' + normal)
                    sleep(1.5)
                    critico_infernal()
                print('\n')
        elif lv_monster == 3:
            power_monster = power_lv3
            aumento_de_poder()
            if card_monster == 'Infernal':
                utils.Musics.boss.play()
                print(red + '   VOCÊ ENCONTROU UM BOSS INFERNAL NIVEL 10')
                if skipBoss >= 1:
                    print(green + '    Você possui um item para Fugir!')
                    print('    Deseja Fugir?')
                    print(green + '                 Sim' + yellow + ' / ' + red + 'Não              ' + normal)
                    escolha_usar_item = str(input('    --> ')).upper().strip()
                    if escolha_usar_item == 'SIM' or escolha_usar_item == 'S':
                        utils.Musics.selecionar.play()
                        print(ciano + '    Você Fugiu!')
                        print(ciano + '    Seu item foi Consumido!')
                        skipBoss = skipBoss - 1
                        card_monster = random.choice(monsters)
                        lv_monster = random.randint(1, 4)
                        sleep(1.5)
                    else:
                        utils.Musics.selecionar.play()
                        print(ciano + '    Você não usou o item!')
                        power_monster = power_monster + monster_power_lv10
                        lv_monster = 10
                        user_level = user_level - 5
                        power_usuario = power_usuario - 1000
                        print(red + '   DANO CRÍTICO!' + normal)
                        sleep(1.5)
                        critico_infernal()
                elif skipBoss <= 0:
                    power_monster = power_monster + monster_power_lv10
                    lv_monster = 10
                    user_level = user_level - 5
                    power_usuario = power_usuario - 1000
                    print(red + '   DANO CRÍTICO!' + normal)
                    sleep(1.5)
                    critico_infernal()
                print('\n')
        elif lv_monster == 4:
            power_monster = power_lv4
            aumento_de_poder()
            if card_monster == 'Infernal':
                utils.Musics.boss.play()
                print(red + '   VOCÊ ENCONTROU UM BOSS INFERNAL NIVEL 10')
                if skipBoss >= 1:
                    print(green + '    Você possui um item para Fugir!')
                    print('    Deseja Fugir?')
                    print(green + '                 Sim' + yellow + ' / ' + red + 'Não              ' + normal)
                    escolha_usar_item = str(input('    --> ')).upper().strip()
                    if escolha_usar_item == 'SIM' or escolha_usar_item == 'S':
                        utils.Musics.selecionar.play()
                        print(ciano + '    Você Fugiu!')
                        print(ciano + '    Seu item foi Consumido!')
                        skipBoss = skipBoss - 1
                        card_monster = random.choice(monsters)
                        lv_monster = random.randint(1, 4)
                        sleep(1.5)
                    else:
                        utils.Musics.selecionar.play()
                        print(ciano + '    Você não usou o item!')
                        power_monster = power_monster + monster_power_lv10
                        lv_monster = 10
                        user_level = user_level - 5
                        power_usuario = power_usuario - 1000
                        print(red + '   DANO CRÍTICO!' + normal)
                        sleep(1.5)
                        critico_infernal()
                elif skipBoss <= 0:
                    power_monster = power_monster + monster_power_lv10
                    lv_monster = 10
                    user_level = user_level - 5
                    power_usuario = power_usuario - 1000
                    print(red + '   DANO CRÍTICO!' + normal)
                    sleep(1.5)
                    critico_infernal()
                print('\n')
        if choiceBonus > 0 and choice == 1:
            utils.Musics.bonus.play()
            print(green + '    Você Encontrou um item Raro!')
            print('    Recebeu {} de Poder!'.format(powerBonus))
            print(ciano + '    Seu item foi Consumido!')
            choiceBonus = choiceBonus - 1
            power_usuario = power_usuario + powerBonus
            sleep(3)
            print('\n')
        # Condição para ganhar/perder o jogo
        if user_level == 100:
            # Atribuição de valores
            if multiplicador < 2.00:
                multiplicador = 2.00
                valorTotal = (aposta * multiplicador)
                print(green + 'Parabéns!')
                print('   Você venceu a Dungeon!' + normal)
                print('   Pontuação --> ', end='')
                print(f'{point}')
                print('   Batalhas --> {}'.format(cont))
                print(green + '   Valor Acumulado R${:.2f}'.format(valorTotal))
                print(green + '   2x Pela Vitória!' + normal)
                mixer.music.stop()
                utils.Musics.win.play()
                x = int(input(''))
                break
            else:
                valorTotal = aposta * multiplicador
                print(green + 'Parabéns!')
                print('   Você venceu a Dungeon!' + normal)
                print('   Pontuação --> ', end='')
                print(f'{point}')
                print('   Batalhas --> {}'.format(cont))
                print(green + '   Valor Acumulado R${:.2f}'.format(valorTotal))
                mixer.music.stop()
                utils.Musics.win.play()
                x = int(input(''))
                break
        elif power_usuario <= 350 or user_level <= 0:
            # Atribuição de valores
            if point <= 0:
                point = 0
                valorTotal = 0
            else:
                valorTotal = aposta * multiplicador
            print(yellow + '   -x-x-x-x--x-x-x-x--x-x-x-x--x-' + normal)
            print(yellow + '   -x-x-x-x-' + red + 'Você Morreu!' + yellow + '-x-x-x-x-' + normal)
            print(yellow + '   -x-x-x-x--x-x-x-x--x-x-x-x--x-' + normal)
            print('   Pontuação --> ', end='' + green)
            print(f'{point}' + normal)
            print('   Batalhas --> ', end='' + green)
            print(f'{cont}')
            print(green + '   Valor Acumulado R${:.2f}'.format(valorTotal))
            mixer.music.stop()
            utils.Musics.lose.play()
            if card_monster == 'Infernal':
                utils.Musics.roarlose.play()
            x = int(input(''))
            break
        # Contador de batalhas

        cont += 1

        # Informação na tela
        print(green + f'   {usuario}', end=' ')
        print(yellow + f'Lv {user_level}' + normal + ' X ' + red + f'{card_monster}', end=' ')
        print(yellow + f'Lv {lv_monster}')
        print(f'   Power: {power_usuario}' + normal, end='   X')
        print(yellow + f'   Power: {power_monster}' + normal)
        result()
        print('   --> {:.2f}x'.format(multiplicador))
        print('   --> {} Pontos'.format(point))
elif iniciar_jogo == 'NÃO' or iniciar_jogo == 'N':
    print(green + '               Escolheu Bem!' + normal)
    mixer.music.stop()
    utils.Musics.lose.play()
    x = int(input(''))

else:
    print(red + '   Resposta errada!' + normal)
    print('    Jogo Pausado!')
    
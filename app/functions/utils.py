from pygame import mixer
import random

class Musics:
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

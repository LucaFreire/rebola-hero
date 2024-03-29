from operator import contains
import re
from tarfile import REGULAR_TYPES
import pygame
import random
from os import path
import math
import sys
import shelve
import time
from pygame import mixer

pygame.init()
relogio = pygame.time.Clock()

tela = pygame.display.set_mode((800, 600))

main_menu = pygame.image.load("./images/07.png").convert_alpha()
fonte = pygame.font.Font('./images/fonte.ttf', 108)
fontePequena = pygame.font.Font('./images/fonte.ttf', 54)

reboletas_sprite = [pygame.image.load("./images/reboletas/1.png"),
                    pygame.image.load("./images/reboletas/2.png"),
                    pygame.image.load("./images/reboletas/3.png"),
                    pygame.image.load("./images/reboletas/4.png"),
                    pygame.image.load("./images/reboletas/5.png"),
                    pygame.image.load("./images/reboletas/6.png"),
                    pygame.image.load("./images/reboletas/7.png"),
                    pygame.image.load("./images/reboletas/8.png"),
                    pygame.image.load("./images/reboletas/9.png"),
                    pygame.image.load("./images/reboletas/10.png"),
                    pygame.image.load("./images/reboletas/11.png"),
                    pygame.image.load("./images/reboletas/12.png"),
                    pygame.image.load("./images/reboletas/13.png"),
                    pygame.image.load("./images/reboletas/14.png"),
                    pygame.image.load("./images/reboletas/15.png"),
                    pygame.image.load("./images/reboletas/16.png"),
                    pygame.image.load("./images/reboletas/17.png"),
                    pygame.image.load("./images/reboletas/18.png"),
                    pygame.image.load("./images/reboletas/19.png"),
                    pygame.image.load("./images/reboletas/20.png"),
                    pygame.image.load("./images/reboletas/21.png"),
                    pygame.image.load("./images/reboletas/22.png"),
                    pygame.image.load("./images/reboletas/23.png"),
                    pygame.image.load("./images/reboletas/24.png"),
                    pygame.image.load("./images/reboletas/25.png"),
                    pygame.image.load("./images/reboletas/26.png"),
                    pygame.image.load("./images/reboletas/27.png"),
                    pygame.image.load("./images/reboletas/28.png"),
                    pygame.image.load("./images/reboletas/29.png"),
                    pygame.image.load("./images/reboletas/30.png"),
                    pygame.image.load("./images/reboletas/31.png"),
                    pygame.image.load("./images/reboletas/32.png"),
                    pygame.image.load("./images/reboletas/33.png"),
                    pygame.image.load("./images/reboletas/34.png"),
                    pygame.image.load("./images/reboletas/35.png"),
                    pygame.image.load("./images/reboletas/36.png"),
                    pygame.image.load("./images/reboletas/37.png"),
                    pygame.image.load("./images/reboletas/38.png"),
                    pygame.image.load("./images/reboletas/39.png"),
                    pygame.image.load("./images/reboletas/40.png")]

image_sprite = [pygame.image.load("./images/00.png"),
                pygame.image.load("./images/01.png"),
                pygame.image.load("./images/02.png"),
                pygame.image.load("./images/03.png"),
                pygame.image.load("./images/04.png"),
                pygame.image.load("./images/05.png"),
                pygame.image.load("./images/06.png"),
                pygame.image.load("./images/07.png"),
                pygame.image.load("./images/08.png"),
                pygame.image.load("./images/09.png"),
                pygame.image.load("./images/10.png"),
                pygame.image.load("./images/11.png"),
                pygame.image.load("./images/12.png"),
                pygame.image.load("./images/13.png"),
                pygame.image.load("./images/14.png"),
                pygame.image.load("./images/15.png"),
                pygame.image.load("./images/16.png"),
                pygame.image.load("./images/17.png"),
                pygame.image.load("./images/18.png"),
                pygame.image.load("./images/19.png"),
                pygame.image.load("./images/20.png")]

fundolas_sprite = [pygame.image.load("./images/fundolas/r1.png"),
                pygame.image.load("./images/fundolas/r2.png"),
                pygame.image.load("./images/fundolas/r3.png"),
                pygame.image.load("./images/fundolas/r4.png"),
                pygame.image.load("./images/fundolas/r5.png"),
                pygame.image.load("./images/fundolas/r6.png")]

start = False
pontos_atuais = 0
textoX = 10
textoY = 10
recorde = open("rec.txt","r").readlines()[0]
recorde3 = recorde
recordeX = 10
recordeY = 50
vacilos = 0 
vacilosX = 10
vacilosY = 100
intervaloA = 2.8
intervaloB = 3.8
frame_atual = 0
reagulador_de_fps = 0
altura_botoes = 532
frame_atual2 = 0
fundolas_atual = 0

class Bloco:
    def __init__(self, Img, ImgX, ImgY):
        self.Img = Img
        self.ImgX = ImgX
        self.ImgY = ImgY

    def Insert(self, Img, ImgX, ImgY): # Função add Bloco
        tela.blit(Img, (ImgX, ImgY))

def Pressione_Start():
    Enter_Start = fontePequena.render("Pressione SPACE P/ Iniciar", True, (255, 0, 0))  # Mensagem
    tela.blit(Enter_Start, (10, 480))  # Localização da Mensagem

def Mostrar_Pontos(x, y):
    Ponto = fontePequena.render("Pontos: " + str(pontos_atuais), True, (0, 0, 255))
    
    tela.blit(Ponto, (x, y))

def Recorde_Pessoal(x, y, level):
    AltoS = fontePequena.render(f"Recorde: {recorde3}", True, (0, 0, 255))
    tela.blit(AltoS, (x, y))

def Mostrar_Vacilos(x, y, num):
    Vacilo = fontePequena.render("Vacilos: " + str(vacilos) + "/" + str(num), True, (0, 0, 255))
    tela.blit(Vacilo, (x, y))

# Blocos Vermelhos
RedImg = pygame.image.load(path.join("images", "bloco_vermelho.png")).convert()
RedX = 274
RedY = random.randint(-1472, -128)
Red_Movimento = random.uniform(intervaloA, intervaloB)
Bloco_Red = Bloco(RedImg, RedX, RedY)

# Blocos Azul
AzulImg = pygame.image.load(path.join("images", "bloco_azul.png")).convert()
AzulX = 462
AzulY = random.randint(-1472, -128)
Azul_Movimento = random.uniform(intervaloA, intervaloB)
Bloco_Azul = Bloco(AzulImg, AzulX, AzulY)

# Blocos Roxo
RoxoImg = pygame.image.load(path.join("images", "bloco_roxo.png")).convert()
RoxoX = 368
RoxoY = random.randint(-1472, -128)
Roxo_Movimento = random.uniform(intervaloA, intervaloB)
Bloco_Roxo = Bloco(RoxoImg, RoxoX, RoxoY)

# Botão Esquerdo
EsquerdoB = pygame.image.load(path.join("images", "botao_esquerdo_pressionado.png"))

# Botão Direito
DireitoB = pygame.image.load(path.join("images", "botao_direito_pressionado.png"))

# Botão Up
UpB = pygame.image.load(path.join("images", "botao_cima_pressionado.png"))

# Sistema de Colisão
def Colisao(BlocoX, BlocoY, BotaoX, BotaoY):
    distancia = math.sqrt((math.pow(BlocoX - BotaoX, 2)) + (math.pow(BlocoY - BotaoY, 2)))  # Cálculo de Colisão
    if distancia < 72:
        return True
    else:
        return False

# Mudança de Dificuldade
def Aumentar_Dificuldade():
    global intervaloA
    global intervaloB
    if pontos_atuais % 10 == 0:  # A Dificuldade aumenta a cada 10 pontos Conquistados
        intervaloA += 0.45
        intervaloB += 0.45

# Reseta Tudo


# Classe Status do Game
class Status_Game:
    def __init__(self):
        self.done = False
        self.next = None
        self.quit = False
        self.previous = None

class Menu(Status_Game):
    def __init__(self):
        Status_Game.__init__(self)
        self.next = "level"
        mixer.music.load(path.join("sounds","favela_bc.mp3"))
        mixer.music.play(1,0.0)

        
    def Pygame_Evento(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            position = pygame.mouse.get_pos() 

            # Se o mouse clicar e estiver na área do start, tocar efeito sonoto e desativa menu
            if ((position[0] > 25 and position[0] < 220) and (position[1] > 373 and position[1] < 449)):
                mixer.music.load(path.join("sounds","favela_bc.mp3"))
                mixer.music.play(1,0.0)
                self.next = "level"
                self.done = True
            
            # se o mouse clicar e estivar no quit, tocar efeito sonoro e sair
            elif ((position[0] > 25 and position[0] < 220) and (position[1] > 510 and position[1] < 585)):
                mixer.music.load(path.join("sounds","favela_bc.mp3"))
                mixer.music.play(1,0.0)
                pygame.quit()
                exit()


    def update(self, Tela):
        global frame_atual
        global reagulador_de_fps

        Game.clock.tick(13)
        # Volta para primeira imagem, gerando o loop
        if frame_atual >= len(image_sprite):
            frame_atual = 0

        # Seta a imagem atual
        image = image_sprite[frame_atual]
        frame_atual += 1
    
        # Da o update na tela
        Tela.blit(image, (0, 0))

    def draw(self, Tela):
        Tela.fill((0,0,0))
        Tela.blit(main_menu, (0, 0))


Personagem = [pygame.image.load("./images/personagem/1.png"),
                pygame.image.load("./images/personagem/2.png"),
                pygame.image.load("./images/personagem/3.png"),
                pygame.image.load("./images/personagem/4.png"),
                pygame.image.load("./images/personagem/5.png"),
                pygame.image.load("./images/personagem/6.png"),
                pygame.image.load("./images/personagem/7.png"),
                pygame.image.load("./images/personagem/8.png"),
                pygame.image.load("./images/personagem/9.png"),
                pygame.image.load("./images/personagem/10.png"),
                pygame.image.load("./images/personagem/11.png"),
                pygame.image.load("./images/personagem/12.png"),
                pygame.image.load("./images/personagem/13.png"),
                pygame.image.load("./images/personagem/14.png"),
                pygame.image.load("./images/personagem/15.png"),
                pygame.image.load("./images/personagem/16.png"),
                pygame.image.load("./images/personagem/17.png"),
                pygame.image.load("./images/personagem/18.png"),
                pygame.image.load("./images/personagem/19.png"),
                pygame.image.load("./images/personagem/20.png"),
                pygame.image.load("./images/personagem/21.png"),
                pygame.image.load("./images/personagem/22.png"),
                pygame.image.load("./images/personagem/23.png"),
                pygame.image.load("./images/personagem/24.png"),
                pygame.image.load("./images/personagem/25.png"),
                pygame.image.load("./images/personagem/26.png"),
                pygame.image.load("./images/personagem/27.png"),
                pygame.image.load("./images/personagem/28.png"),
                pygame.image.load("./images/personagem/29.png"),
                pygame.image.load("./images/personagem/30.png"),
                pygame.image.load("./images/personagem/31.png"),
                pygame.image.load("./images/personagem/32.png"),
                pygame.image.load("./images/personagem/33.png"),
                pygame.image.load("./images/personagem/34.png"),
                pygame.image.load("./images/personagem/35.png"),
                pygame.image.load("./images/personagem/36.png"),
                pygame.image.load("./images/personagem/37.png"),
                pygame.image.load("./images/personagem/38.png"),
                pygame.image.load("./images/personagem/39.png"),
                pygame.image.load("./images/personagem/40.png"),
                pygame.image.load("./images/personagem/41.png"),
                pygame.image.load("./images/personagem/42.png"),
                pygame.image.load("./images/personagem/43.png"),
                pygame.image.load("./images/personagem/44.png"),
                pygame.image.load("./images/personagem/45.png"),
                pygame.image.load("./images/personagem/46.png"),
                pygame.image.load("./images/personagem/47.png"),
                pygame.image.load("./images/personagem/48.png")]


# Classe do Nível
class Level(Status_Game):
    def __init__(self):
        Status_Game.__init__(self)
        self.next = "level"
        frame_atual2 = 0
        mixer.music.load(path.join("sounds","MusicTue.mp3"))
        mixer.music.play(1,0.0)

    def Pygame_Evento(self, event):
        global start, RedY, AzulY, RoxoY, Vacilos, Red_Movimento, \
            Azul_Movimento, Roxo_Movimento, pontos_atuais, Direito_Pressionado, \
            Esquerdo_Pressionado, Up_Pressionado, frame_atual2

        Colisao_Red = Colisao(RedX, RedY, RedX, altura_botoes)
        Colisao_Azul = Colisao(AzulX, AzulY, AzulX, altura_botoes)
        Colisao_Roxo = Colisao(RoxoX, RoxoY, RoxoX, altura_botoes)

        if event.type == pygame.KEYDOWN:

            # Botão para Iniciar
            if event.key == pygame.K_SPACE:
                start = True

            # Botão Esquerdo
            if event.key == pygame.K_LEFT:
                if Colisao_Red:
                    # SOM sound = mixer.Sound(path.join("Game Assets", "collison.wav"))
                    # sound.play()
                    pontos_atuais += 1
                    RedY = random.randint(-1472, -128)
                    Aumentar_Dificuldade()
                    Red_Movimento = random.uniform(intervaloA, intervaloB)

            # Botão Direiro
            if event.key == pygame.K_RIGHT:
                if Colisao_Azul:
                    # SOM sound = mixer.Sound(path.join("Game Assets", "collison.wav"))
                    # sound.play()
                    pontos_atuais += 1
                    AzulY = random.randint(-1472, -128)
                    Aumentar_Dificuldade()
                    Azul_Movimento = random.uniform(intervaloA, intervaloB)

            # Botão UP
            if event.key == pygame.K_UP:
                if Colisao_Roxo:
                    # SOM sound = mixer.Sound(path.join("Game Assets", "collison.wav"))
                    # sound.play()
                    pontos_atuais += 1
                    RoxoY = random.randint(-1472, -128)
                    Aumentar_Dificuldade()
                    Roxo_Movimento = random.uniform(intervaloA, intervaloB)
            frame_atual2 += 1

    def update(self, Tela):
        self.draw(Tela)
        global RedY, AzulY, RoxoY, vacilos, Red_Movimento, Roxo_Movimento, Azul_Movimento, \
        recorde, start, pontos_atuais, intervaloA, intervaloB, frame_atual2, fundolas_atual, recorde3

        
        if start == False:
            Pressione_Start()

        if (frame_atual2 == 48):
            frame_atual2 = 0
            image_sprite2 = Personagem[frame_atual2]
        else:
            image_sprite2 = Personagem[frame_atual2]

        image_sprite2 = pygame.transform.scale(image_sprite2, (150,300))

        Tela.blit(image_sprite2, (480, 190))

        if RedY >= 574:
            Percas = mixer.Sound(path.join("sounds","perca.wav"))
            Percas.play()
            vacilos += 1
            RedY = random.randint(-1472, -128)

        if AzulY >= 574:
            Percas = mixer.Sound(path.join("sounds","perca.wav"))
            Percas.play()
            vacilos += 1
            AzulY = random.randint(-1472, -128)

        if RoxoY >= 574:
            Percas = mixer.Sound(path.join("sounds","perca.wav"))
            Percas.play()
            vacilos += 1
            RoxoY = random.randint(-1472, -128)

        if vacilos == 7:  # Número de Vidas

            RedY = -64
            Red_Movimento = 0

            AzulY = -64
            Azul_Movimento = 0

            RoxoY = -64
            Roxo_Movimento = 0

            if pontos_atuais > int(recorde):
                recorde = open("rec.txt", "w")
                recorde = recorde.write(str(pontos_atuais))
                recorde3 = pontos_atuais

            time.sleep(0.5)
            start = False
            pontos_atuais = 0
            vacilos = 0

            intervaloA = 2.8
            intervaloB = 3.8

            RoxoX = random.randint(-1472, -128)
            RedY = random.randint(-1472, -128)
            AzulX = random.randint(-1472, -128)
            Red_Movimento = random.uniform(intervaloA, intervaloB)

            Azul_Movimento = random.uniform(intervaloA, intervaloB)

            Roxo_Movimento = random.uniform(intervaloA, intervaloB)

            self.done = True
            self.next = "main_menu"

        while start:
            RedY += Red_Movimento
            RoxoY += Roxo_Movimento
            AzulY += Azul_Movimento
            break

    def draw(self, Tela):

        global fundolas_atual

        if (int(fundolas_atual) == 39):
            Fundo_Fase = reboletas_sprite[int(fundolas_atual)]
            fundolas_atual = 0
        else:
            Fundo_Fase = reboletas_sprite[int(fundolas_atual)]
            fundolas_atual += 0.05

        Tela.fill((0, 0, 0))
        Tela.blit(Fundo_Fase, (0, 0))  # Imagem de fundo da Fase
        Tela.blit(EsquerdoB, (RedX, altura_botoes))
        Tela.blit(DireitoB, (AzulX, altura_botoes))
        Tela.blit(UpB, (RoxoX, altura_botoes))

        Bloco_Red.Insert(RedImg, RedX, RedY), Bloco_Azul.Insert(AzulImg, AzulX, AzulY), Bloco_Roxo.Insert(RoxoImg,RoxoX, RoxoY)
        Mostrar_Pontos(textoX, textoY), Mostrar_Vacilos(vacilosX, vacilosY, 7), Recorde_Pessoal(recordeX, recordeY, "level")


class Controle_Jogo:
    def __init__(self):
        self.__dict__.update()
        self.done = False
        self.Tela = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()

    def Setup(self, Levels, Menu_Principal):
        self.Levels = Levels
        self.Levels_Nome = Menu_Principal
        self.state = self.Levels[self.Levels_Nome]

    def Troca(self):
        self.state.done = False
        previous = self.Levels_Nome
        self.Levels_Nome = self.state.next
        self.state = self.Levels[self.Levels_Nome]
        self.state.previous = previous

    def update(self,df):
        if self.state.quit:
            self.done = True
        elif self.state.done:
            self.Troca()
        self.state.update(self.Tela)

    def Loop_De_Eventos(self):
        for Eventos in pygame.event.get():
            if Eventos.type == pygame.QUIT:
                self.done = True
            self.state.Pygame_Evento(Eventos)

    def Loop_Principal(self):
        while not self.done:
            Tempo = self.clock.tick(120) / 1000.0
            self.Loop_De_Eventos()
            self.update(Tempo)
            pygame.display.update()


Game = Controle_Jogo()
levels = {
    'main_menu': Menu(),
    'level':Level()
}

Game.Setup(levels, 'main_menu')
Game.Loop_Principal()
pygame.quit()
sys.exit()

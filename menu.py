from tkinter import font
import pygame
from pygame.locals import *
from os import path
from pygame import mixer
import sys
import math
import random
import time

# # Inicia jogo
pygame.init()
 
# Define tamanho de tela
tela = pygame.display.set_mode((800, 600))
 
# Carrega imagens da tela principal em uma lista
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
                pygame.image.load("./images/20.png"),]
 
# Cria objeto para ler tempo
clock = pygame.time.Clock()
 
# Seta algumas varíaveis globais para serem usadas posteriormente
run = True
frame_atual = 0
menu = True
pontos_atuais = 0
fonte = pygame.font.Font('disposabledroid-bb.regular.ttf', 108)

fontex = 0
fontey = 0

def apareceTexto():
    global fontex
    global fontey
    global pontos_atuais
    global tela
    pontos_atuais+= 1
    texto = str(pontos_atuais)

    score = fonte.render(texto, 1, (255,255,255))
    image = pygame.image.load("./images/jesuis.png")

    tela.blit(image, (0, 0))
    tela.blit(score, (0,0))
    
    pygame.display.update()
    
    print("Working")
    

def carrega_menu():
    global menu

    while(menu):
        
        global frame_atual

        # Troca os frames a cada 13 milisegundos
        clock.tick(13)

        # Volta para primeira imagem, gerando o loop
        if frame_atual >= len(image_sprite):
            frame_atual = 0

        # Seta a imagem atual
        image = image_sprite[frame_atual]
    
        # Da o update na tela
        tela.blit(image, (0, 0))
        pygame.display.update()


        frame_atual += 1

        # Verifica eventos do pygame
        for event in pygame.event.get():
            # Se o botão x for clicado, fechar jogo
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            # Pega inputs do mouse
            if (event.type == pygame.MOUSEBUTTONUP):
                # Armazena a posição xy do mouse em uma tupla
                position = pygame.mouse.get_pos()

                # Se o mouse clicar e estiver na área do start, tocar efeito sonoto e desativa menu
                if ((position[0] > 25 and position[0] < 220) and (position[1] > 373 and position[1] < 449)):
                    mixer.music.load(path.join("sounds","entrada_leaderboard.wav"))
                    mixer.music.play(1,0.0)

                    while pygame.mixer.music.get_busy() == True:
                        continue

                    menu = False

                # se o mouse clicar e estivar no quit, tocar efeito sonoro e sair
                elif ((position[0] > 25 and position[0] < 220) and (position[1] > 510 and position[1] < 585)):
                    mixer.music.load(path.join("sounds","entrada_leaderboard.wav"))
                    mixer.music.play(1,0.0)
                    while pygame.mixer.music.get_busy() == True:
                        continue
                    pygame.quit()
                    exit()


def leaderboard():
    # Carrega musica de fundo
    mixer.music.load(path.join("sounds","favela_bc.mp3"))
    mixer.music.play(-1)
    # Carrega imagem de fundo
    image = pygame.image.load("./images/jesuis.png")

    tela.blit(image, (0, 0))
    pygame.display.update()
    

# Toca musica do menu, carrega ele e quando sair do menu inicia a tela de leaderboard
mixer.music.load(path.join("sounds","favela_bc.mp3"))
mixer.music.play(-1)
carrega_menu()
leaderboard()

# # Roda eternamente verificações para realizar ações no jogo
# while run:

#     for event in pygame.event.get():
        
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             exit()
        
#         if (event.type == pygame.KEYDOWN):
            
#             apareceTexto()


from tkinter import font
import pygame
from pygame.locals import *
from os import path
from pygame import mixer

# Inicia jogo
pygame.init()
 
# Define tamanho de tela
window = pygame.display.set_mode((800, 600))
 
# Carrega imagens da tela principal em uma lista
image_sprite = [pygame.image.load("./images_menu/00.png"),
                pygame.image.load("./images_menu/01.png"),
                pygame.image.load("./images_menu/02.png"),
                pygame.image.load("./images_menu/03.png"),
                pygame.image.load("./images_menu/04.png"),
                pygame.image.load("./images_menu/05.png"),
                pygame.image.load("./images_menu/06.png"),
                pygame.image.load("./images_menu/07.png"),
                pygame.image.load("./images_menu/08.png"),
                pygame.image.load("./images_menu/09.png"),
                pygame.image.load("./images_menu/10.png"),
                pygame.image.load("./images_menu/11.png"),
                pygame.image.load("./images_menu/12.png"),
                pygame.image.load("./images_menu/13.png"),
                pygame.image.load("./images_menu/14.png"),
                pygame.image.load("./images_menu/15.png"),
                pygame.image.load("./images_menu/16.png"),
                pygame.image.load("./images_menu/17.png"),
                pygame.image.load("./images_menu/18.png"),
                pygame.image.load("./images_menu/19.png"),
                pygame.image.load("./images_menu/20.png"),]
 
# Cria objeto para ler tempo
clock = pygame.time.Clock()
 
# Seta algumas varíaveis globais para serem usadas posteriormente
run = True
value = 0
menu = True
pontos_atuais = 0
fonte = pygame.font.Font('disposabledroid-bb.regular.ttf', 108)

fontex = 0
fontey = 0

def apareceTexto():
    global fontex
    global fontey
    global pontos_atuais
    global window
    pontos_atuais+= 1
    texto = str(pontos_atuais)

    score = fonte.render(texto, 1, (255,255,255))
    image = pygame.image.load("./images_menu/jesuis.png")

    window.blit(image, (0, 0))
    window.blit(score, (0,0))
    
    pygame.display.update()
    
    print("Working")
    

def carrega_menu():
    global menu

    while(menu):
        
        global value

        # Troca os frames a cada 13 milisegundos
        clock.tick(13)

        # Volta para primeira imagem, gerando o loop
        if value >= len(image_sprite):
            value = 0

        # Seta a imagem atual
        image = image_sprite[value]
    
        # Da o update na tela
        window.blit(image, (0, 0))
        pygame.display.update()
    
        window.fill((0, 0, 0))

        value += 1

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
    image = pygame.image.load("./images_menu/jesuis.png")

    window.blit(image, (0, 0))
    pygame.display.update()
    
    window.fill((0, 0, 0))

# Toca musica do menu, carrega ele e quando sair do menu inicia a tela de leaderboard
mixer.music.load(path.join("sounds","favela_bc.mp3"))
mixer.music.play(-1)
carrega_menu()
leaderboard()

# Roda eternamente verificações para realizar ações no jogo
while run:

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if (event.type == pygame.KEYDOWN):
            
            apareceTexto()
        
    
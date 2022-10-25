import pygame
from pygame.locals import *
from os import path
from pygame import mixer

pygame.init()
 
window = pygame.display.set_mode((800, 600))
 
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
 
clock = pygame.time.Clock()
 
run = True
value = 0
menu = True

while run:

    def leaderboard():
        image = pygame.image.load("./images_menu/jesuis.png")
        
        window.blit(image, (0, 0))
        pygame.display.update()
        
        window.fill((0, 0, 0))

    def carrega_menu():
        global menu

        while(menu):
            
            global value

            clock.tick(13)

            if value >= len(image_sprite):
                value = 0

            image = image_sprite[value]
        
            window.blit(image, (0, 0))
            pygame.display.update()
        
            window.fill((0, 0, 0))

            value += 1

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if (event.type == pygame.MOUSEBUTTONUP):
                    position = pygame.mouse.get_pos()

                    if ((position[0] > 25 and position[0] < 220) and (position[1] > 373 and position[1] < 449)):
                        menu = False
                    elif ((position[0] > 25 and position[0] < 220) and (position[1] > 510 and position[1] < 585)):
                        pygame.quit()
                        exit()
    

    mixer.music.load(path.join("sounds","favela_bc.mp3"))
    mixer.music.play(-1)
    carrega_menu()
    leaderboard()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if (event.type == pygame.KEYDOWN):
            
            print("Uma tecla foi pressionada")

        
    


        



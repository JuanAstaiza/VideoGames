'''
    Devloper: JuanAstaiza
    Date: 30-Sep-2021
    Description:
        Desarrollo de la version 1.0 de un video juego de atari
'''

#Importar librerias
import sys
import pygame

pygame.init()

#Classes
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.img_ball = pygame.image.load('images/bolita.png')
        self.rect = self.img_ball.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.centerx = HEIGHT / 2

#General settings
WIDTH = 640
HEIGHT = 480

screen = pygame.display.set_mode( (WIDTH,  HEIGHT) )
pygame.display.set_caption('Atari')
icon = pygame.image.load('images/main_icon.png')
pygame.display.set_icon(icon)

ball = Ball()

#Loop (Revisión cíclica de los eventos) => Listener
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #Draw de la ball
    screen.blit(ball.img_ball, ball.rect)
    #Refresh de elementos en screen
    pygame.display.flip()
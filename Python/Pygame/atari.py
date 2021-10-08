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

##################################################################################################

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.img_ball = pygame.image.load('images/bolita.png')
        self.rect = self.img_ball.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.centery = HEIGHT / 2
        # [Param1 -> Veloc del mov. / Param2 -> Amplitud del mov]
        # A mayor amplitud rebote afecta eje Y y a menor amplitud rebote afecte eje X.
        self.speed = [2,2] #[]

    def pibot(self):
        #validate Y <- ¡! - >
        if self.rect.bottom >= HEIGHT or self.rect.top <=0:
            self.speed[1] = -self.speed[1]
        elif self.rect.right >= WIDTH or self.rect.left <=0:
            self.speed[0] = -self.speed[0]
        #validate x <- x ->
        self.rect.move_ip(self.speed)


##################################################################################################

class Bar(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.img_bar = pygame.image.load('images/paleta.png')
        self.rect = self.img_bar.get_rect()
        self.rect.midbottom = (WIDTH / 2,HEIGHT-10)
        self.speed = [0,0] # []

    def slide(self,listener):
        if listener.key == pygame.K_LEFT and self.rect.left > 0 :
            self.speed = [-5,0]
        elif listener.key == pygame.K_RIGHT and self.rect.right < WIDTH:
            self.speed =  [5,0]
        else:
            self.speed = [0,0]

        self.rect.move_ip(self.speed)

##################################################################################################
#ladrillo
class Brick(pygame.sprite.Sprite):
    def __init__(self,position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/ladrillo.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = position
#Muro
class Wall(pygame.sprite.Group):
    def __init__(self,totalBrick):
        pygame.sprite.Group.__init__(self)
        posX = 0
        posY = 10

        for i in range(totalBrick):
            brick = Brick(( posX,posY ))
            self.add(brick)

            posX += brick.rect.width
            if posX >= WIDTH :
                posX = 0
                posY += brick.rect.height

##################################################################################################



#General settings
WIDTH = 640
HEIGHT = 480

BG_COLOR = (4,152,231)

screen = pygame.display.set_mode( (WIDTH,  HEIGHT) )
pygame.display.set_caption('Atari')
icon = pygame.image.load('images/main_icon.png')
pygame.display.set_icon(icon)

game_clock = pygame.time.Clock()
pygame.key.set_repeat(20)


ball = Ball()
player = Bar()
totalBricks=int(input("Digita la cantidad de ladrillos a generar: "))
wall = Wall(totalBricks)

#Loop (Revisión cíclica de los eventos) => Listener
while True:
    game_clock.tick(60)
    for event in pygame.event.get():
        # Verifica si se preciono la letra x de la ventana
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Verifica si el jugador precionó tela del teclado
        elif event.type == pygame.KEYDOWN:
            player.slide(event)


    #call pibot
    ball.pibot()

    #collisions between bar and ball

    #Cambio de trayectoria de la bola
    if pygame.sprite.collide_rect(ball,player):  #Player is the bar.
         ball.speed[1]=-ball.speed[1]

    # Collisions between ball and wall (bricks)Destroy bricks
    #sprite el objeto principal. balon Accionar
    #group el objeto que se va a chocar  los ladrillos.

    elements =  pygame.sprite.spritecollide(ball,wall,False,collided=None)
    if elements : #Mientras existan ladrillos para chocar.
        brink = elements[0]
        centx = ball.rect.centerx
        if centx < brink.rect.left or centx > brink.rect.right:
            #Afectamos velocidad
            ball.speed[0] = -ball.speed[0]
        else:
            # Afectamos trayectoria
            ball.speed[1] = -ball.speed[1]
        wall.remove(brink)



    #set Background Color
    screen.fill(BG_COLOR)
    #Draw de la ball
    screen.blit(ball.img_ball, ball.rect)
    #Draw de la bar
    screen.blit(player.img_bar, player.rect)
    #Draw muro
    wall.draw(screen)
    #Refresh de elementos en screen
    pygame.display.flip()
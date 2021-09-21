#Devloper: JuanAstaiza
#Date: 20-Sep-2021

'''
    Descripción: Este es nuestro primer script pyhton con Python.
    Este script genera una ventana en PyGame con el título  ¡Hello world!
'''

#1. Importar librerias / paquetes
import pygame
import sys

# 2. Inicializar Pygame
pygame.init();

# 3. Dimenzionar (w x h) el tamaño de la ventana del video juego
# Configuraciones generales de la ventana (WxH,title,Color)

width=800
height=400
mywindow=pygame.display.set_mode((width,height))
pygame.display.set_caption("Number Race v 1.0")

# Setear Colores R(red) G (Green) B (Blue) => HxD
# RGB => 0-225

#Primera opción
white = pygame.Color(255,255,255)
red = pygame.Color(255,0,0)
green = pygame.Color(0,255,0)
blue = pygame.Color(0,0,255)
x = pygame.Color(140,217,150)
y = pygame.Color(255,229,143)
#Segunda opción
bgColor = (100,100,100)

#Figuras
##Restangulo
rect1=pygame.Rect(150,300,150,50)  #x,y,w,h
rect2=pygame.Rect(350,230,150,50)  #x,y,w,h

rect1.center = (width // 2,height // 2)
#El punto medio 800 (División de asignación) - CALCULA EL ALTO DE LA PANTALLA PARA SABER EL PUNTO INTEMEDIO

print(rect2.x)
print(rect2.y)

##Circulo

#4. Mantener visible / abierta la ventana en pantalla
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Valida si usuario presionó cerrar x
            pygame.quit() # Cierra la ventana
            sys.exit() # Cierra
    mywindow.fill(x)
    pygame.draw.rect(mywindow,red,rect1) # contexto (ventana) ,color ,rectangulo
    pygame.draw.rect(mywindow,blue,rect2) # contexto (ventana) ,color ,rectangulo

    pygame.draw.rect(mywindow,green,(50,50,50,50))
    pygame.draw.line(mywindow,red,(10,10),(300,10),5)
    pygame.draw.circle(mywindow,y,(400,200),100)
    pygame.draw.polygon(mywindow, blue,((0,300), (100,200),(200,300)))

    pygame.display.update()
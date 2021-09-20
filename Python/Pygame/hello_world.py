#Devloper: JuanAstaiza
#Date: 20-Sep-2021

'''
    Descripción: Este es nuestro primer script pyhton con Python.
    Este script genera una ventana en PyGame con el título  ¡Hello world!
'''

#1. Importar librerias / paquetes
import pygame
import sys

#2. Inicializar Pygame
pygame.init();

#3. Dimenzionar (w x h) el tamaño de la ventana del videojuego
width=800
height=400
window=pygame.display.set_mode((width,height))
pygame.display.set_caption("Number Race v1")

#4. Mantener visible / abierta la ventana en pantalla
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #valida si usuario presionó cerrar x
            pygame.quit(); #Cierra la ventana
            sys.exit(); #cierra
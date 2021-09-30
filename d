[33mcommit 81514fa279fa4f46b65f4d0688a1756c87939756[m[33m ([m[1;36mHEAD -> [m[1;32mmain[m[33m, [m[1;31morigin/main[m[33m, [m[1;31morigin/HEAD[m[33m)[m
Author: JuanAstaiza <juancarlosastaiza@gmail.com>
Date:   Tue Sep 21 15:19:07 2021 -0500

     Clase 21-09-2021 Actualización Mi primera Ventana (Colores,figuras, entre otros.)

[1mdiff --git a/Python/Pygame/hello_world.py b/Python/Pygame/hello_world.py[m
[1mindex 301a68b..d26b4c2 100644[m
[1m--- a/Python/Pygame/hello_world.py[m
[1m+++ b/Python/Pygame/hello_world.py[m
[36m@@ -10,18 +10,56 @@[m
 import pygame[m
 import sys[m
 [m
[31m-#2. Inicializar Pygame[m
[32m+[m[32m# 2. Inicializar Pygame[m
 pygame.init();[m
 [m
[31m-#3. Dimenzionar (w x h) el tamaño de la ventana del videojuego[m
[32m+[m[32m# 3. Dimenzionar (w x h) el tamaño de la ventana del video juego[m
[32m+[m[32m# Configuraciones generales de la ventana (WxH,title,Color)[m
[32m+[m
 width=800[m
 height=400[m
[31m-window=pygame.display.set_mode((width,height))[m
[31m-pygame.display.set_caption("Number Race v1")[m
[32m+[m[32mmywindow=pygame.display.set_mode((width,height))[m
[32m+[m[32mpygame.display.set_caption("Number Race v 1.0")[m
[32m+[m
[32m+[m[32m# Setear Colores R(red) G (Green) B (Blue) => HxD[m
[32m+[m[32m# RGB => 0-225[m
[32m+[m
[32m+[m[32m#Primera opción[m
[32m+[m[32mwhite = pygame.Color(255,255,255)[m
[32m+[m[32mred = pygame.Color(255,0,0)[m
[32m+[m[32mgreen = pygame.Color(0,255,0)[m
[32m+[m[32mblue = pygame.Color(0,0,255)[m
[32m+[m[32mx = pygame.Color(140,217,150)[m
[32m+[m[32my = pygame.Color(255,229,143)[m
[32m+[m[32m#Segunda opción[m
[32m+[m[32mbgColor = (100,100,100)[m
[32m+[m
[32m+[m[32m#Figuras[m
[32m+[m[32m##Restangulo[m
[32m+[m[32mrect1=pygame.Rect(150,300,150,50)  #x,y,w,h[m
[32m+[m[32mrect2=pygame.Rect(350,230,150,50)  #x,y,w,h[m
[32m+[m
[32m+[m[32mrect1.center = (width // 2,height // 2)[m
[32m+[m[32m#El punto medio 800 (División de asignación) - CALCULA EL ALTO DE LA PANTALLA PARA SABER EL PUNTO INTEMEDIO[m
[32m+[m
[32m+[m[32mprint(rect2.x)[m
[32m+[m[32mprint(rect2.y)[m
[32m+[m
[32m+[m[32m##Circulo[m
 [m
 #4. Mantener visible / abierta la ventana en pantalla[m
 while True:[m
     for event in pygame.event.get():[m
[31m-        if event.type == pygame.QUIT: #valida si usuario presionó cerrar x[m
[31m-            pygame.quit(); #Cierra la ventana[m
[31m-            sys.exit(); #cierra[m
\ No newline at end of file[m
[32m+[m[32m        if event.type == pygame.QUIT: # Valida si usuario presionó cerrar x[m
[32m+[m[32m            pygame.quit() # Cierra la ventana[m
[32m+[m[32m            sys.exit() # Cierra[m
[32m+[m[32m    mywindow.fill(x)[m
[32m+[m[32m    pygame.draw.rect(mywindow,red,rect1) # contexto (ventana) ,color ,rectangulo[m
[32m+[m[32m    pygame.draw.rect(mywindow,blue,rect2) # contexto (ventana) ,color ,rectangulo[m
[32m+[m
[32m+[m[32m    pygame.draw.rect(mywindow,green,(50,50,50,50))[m
[32m+[m[32m    pygame.draw.line(mywindow,red,(10,10),(300,10),5)[m
[32m+[m[32m    pygame.draw.circle(mywindow,y,(400,200),100)[m
[32m+[m[32m    pygame.draw.polygon(mywindow, blue,((0,300), (100,200),(200,300)))[m
[32m+[m
[32m+[m[32m    pygame.display.update()[m
\ No newline at end of file[m

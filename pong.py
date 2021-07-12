import pygame, sys, random, time

from pygame.constants import K_DOWN, K_UP, K_s, K_w
from constantes import *
#funciones
from funciones import raqueta, pelota, cancha, texto, close_verify, refresh_screen

#constantes
gameOver = False
pause = False
pos_y1 = 200
pos_y2 = 200
pelotaY = random.randint(96, 444)
pelotaX = 400
contadorJ1 = 0
contadorJ2 = 0

pygame.init()
tecla = pygame.key.get_pressed()
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

#bucle principal
while gameOver  == False:
    
    close_verify()
    screen.fill(negro)
    #contorno(screen, blanco, 20, 30, 760, 440, 5)
    cancha(screen, blanco,400, 30, 440, 50, 1)
    texto(screen, blanco, 600, 60, 55, str(contadorJ2).zfill(2), consolas)
    texto(screen, blanco, 200, 60, 55, str(contadorJ1).zfill(2), consolas)
   
    tecla = pygame.key.get_pressed()
    if(tecla[K_s]):          
        if (pos_y1 < 350 and pos_y1 >= 90):
            pos_y1 += speed
    elif(tecla[K_w]):
        if (pos_y1 <= 355 and pos_y1 > 90):
            pos_y1 -= speed
    else:
        pass
    tecla = pygame.key.get_pressed()
    if(tecla[K_DOWN]):          
        if (pos_y2 < 350 and pos_y2 >= 90):
            pos_y2 += speed
    elif(tecla[K_UP]):
        if (pos_y2 <= 355 and pos_y2 > 90):
            pos_y2 -= speed
    else:
        pass
    if (pelotaX <= 32 or pelotaX >= 770):
        speedPelotaX *= -1
    if (pelotaY <= 95 or pelotaY >= 445):
        speedPelotaY *= -1

    if(contadorJ1 ==  5):
        gameOver = True  
    elif(contadorJ2 == 5):
        gameOver = True        
        
    if(pelotaY - 5 >= pos_y1 and pelotaY  -5 <= pos_y1 + 100):
        if(pelotaX <= 90 and pelotaX >= 70):
            speedPelotaX *= -1

    if(pelotaX < 65):
        contadorJ2 += 1
        if(contadorJ2 < 5):
            pelotaX = 400 
            screen.fill(negro)
            texto(screen, blanco, 400, 200, 30, "Jugador 2 a anotado!!", consolas)  
            refresh_screen(clock, 60)
            pygame.time.delay(1000)


    pelotaX += speedPelotaX
    pelotaY += speedPelotaY
    pelota(screen, blanco, pelotaX, pelotaY, 10)
    raqueta(screen, blanco, 70, pos_y1, 100, 20)
    raqueta(screen, blanco, 710, pos_y2, 100, 20)
    
    refresh_screen(clock, 60)

screen.fill(negro)
texto(screen, blanco, 400, 200, 30, "FIN DE JUEGO", consolas)  
refresh_screen(clock, 60)
pygame.time.delay(1000)




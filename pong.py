import pygame, sys, random, time

from pygame.constants import K_DOWN, K_UP, K_s, K_w
from constantes import *
#funciones
from funciones import cancha, texto, close_verify, refresh_screen

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
sound = pygame.mixer.Sound("sonidos/rebote.ogg")
#bucle principal
while gameOver  == False:
    
    close_verify()
    screen.fill(negro)

    #crea los elementos del juego 
    #contorno(screen, blanco, 20, 30, 760, 440, 5)
    cancha(screen, blanco,400, 30, 440, 50, 1)
    texto(screen, blanco, 600, 60, 55, str(contadorJ2).zfill(2), consolas)
    texto(screen, blanco, 200, 60, 55, str(contadorJ1).zfill(2), consolas)

    #evaluacion de los puntajes de los jugadores
    if(contadorJ1 ==  5):
        gameOver = True  
    elif(contadorJ2 == 5):
        gameOver = True                    

    #lectura del teclado para el jugador 1
    tecla = pygame.key.get_pressed()
    if(tecla[K_s]):          
        if (pos_y1 < 350 and pos_y1 >= 90):
            pos_y1 += speed
    elif(tecla[K_w]):
        if (pos_y1 <= 355 and pos_y1 > 90):
            pos_y1 -= speed
    else:
        pass
    
    #lectura del teclado para el jugador 2
    tecla = pygame.key.get_pressed()
    if(tecla[K_DOWN]):          
        if (pos_y2 < 350 and pos_y2 >= 90):
            pos_y2 += speed
    elif(tecla[K_UP]):
        if (pos_y2 <= 355 and pos_y2 > 90):
            pos_y2 -= speed
    else:
        pass

    #limite de la pelota  en la cancha
    if (pelotaX <= 32 or pelotaX >= 770):
        speedPelotaX *= -1
        sound.play()
    if (pelotaY <= 95 or pelotaY >= 445):
        speedPelotaY *= -1
        sound.play()

    #mueve la pelota
    pelotaX += speedPelotaX
    pelotaY += speedPelotaY    

    #evalua si la pelota colisiona con la porteria del jugador 1
    if(pelotaX < 65):
        contadorJ2 += 1
        if(contadorJ2 < 5):
            pelotaX = 400 
            screen.fill(negro)
            texto(screen, blanco, 400, 200, 30, "Jugador 2 a anotado!!", consolas)  
            refresh_screen(clock, 60)
            pygame.time.delay(1000)

    #evalua si la pelota colisiona con la porteria del jugador 2
    if(pelotaX > 765):
        contadorJ1 += 1
        if(contadorJ1 < 5):
            pelotaX = 400 
            screen.fill(negro)
            texto(screen, blanco, 400, 200, 30, "Jugador 1 a anotado!!", consolas)  
            refresh_screen(clock, 60)
            pygame.time.delay(1000)            

    #zona de dibujo de los elementos del juego 
    ball = pygame.draw.circle(screen, blanco, (pelotaX, pelotaY),10)
    jugador1 = pygame.draw.rect(screen, blanco, (70, pos_y1, 5, 100))
    jugador2 = pygame.draw.rect(screen, blanco, (710, pos_y2, 5, 100))

    #evalua si la pelota colisiona con la raqueta de los jugadores
    if(ball.colliderect(jugador1) or ball.colliderect(jugador2)):
        speedPelotaX *= -1 
        sound.play()       

    #actualiza la pantalla
    refresh_screen(clock, 60)
#pinta la pantalla y los elementos del juego quedan ocultos
screen.fill(negro)
texto(screen, blanco, 400, 200, 30, "FIN DE JUEGO", consolas) 
if( contadorJ1 <= 5):
    texto(screen, blanco, 400, 250, 30, "jugador 1 gana", consolas) 
if(contadorJ2 <= 5):
    texto(screen, blanco, 400, 250, 30, "jugador 2 gana", consolas) 
refresh_screen(clock, 60)
pygame.time.delay(1000)




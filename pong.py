import pygame, sys, random, time

from pygame.constants import K_DOWN, K_UP
from constantes import *
#funciones
def rectangulo1(screen, color, x, y, largo, ancho):
    pygame.draw.rect(screen, color, (x, y,ancho, largo))
def contorno(screen, color, x, y, largo, alto, ancho):
    pygame.draw.line(screen, color, (x, y), (x + largo, y), ancho)
    pygame.draw.line(screen, color, (x, y-2), (x, y + alto), ancho)
    pygame.draw.line(screen, color, (x, y + alto - 2), (x + largo, y + alto - 2), ancho)
    pygame.draw.line(screen, color, (x + largo, y - 2), (x + largo, y + alto), ancho)

def cancha(screen, color, x, y, largo, radio, ancho):
    pygame. draw.line(screen, color, (x, y), (x, y + largo), ancho)

def texto(screen, color, x, y, dimensiones, texto, fuente):
    tipo_fuente = pygame.font.Font(fuente, dimensiones)
    superficie = tipo_fuente.render(texto, False, color)
    contenedor = superficie.get_rect()
    contenedor.center = (x, y)
    screen.blit(superficie, contenedor)
def pausa():
    sys.stdout.flush()
    time.sleep(1)
    sys.stdout.flush()    
#constantes
gameOver = False
pos_y = 200
pelotaY = random.randint(55, 445)
pelotaX = 400
contador1 = 3

pygame.init()
tecla = pygame.key.get_pressed()
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

#bucle principal
while gameOver  == False:
    
    close_verify()
    screen.fill(negro)
    contorno(screen, blanco, 20, 30, 760, 440, 5)
    cancha(screen, blanco,400, 30, 440, 50, 1)
    texto(screen, blanco, 220, 16, 30, str(contador1), consolas)
    tecla = pygame.key.get_pressed()
    if(tecla[K_DOWN]):          
        if (pos_y < 350 and pos_y >= 50):
            pos_y += speed
    elif(tecla[K_UP]):
        if (pos_y <= 350 and pos_y > 50):
            pos_y -= speed
    else:
        pass
    
    if (pelotaX <= 32 or pelotaX >= 770):
        speedPelotaX *= -1
        #print(f"x: {pelotaX}, y: {pelotaY}")
    if (pelotaY <= 55 or pelotaY >= 445):
        speedPelotaY *= -1
        #print(f"x: {pelotaX}, y: {pelotaY}")
    if(contador1==  5):
        gameOver = True  
    if(pelotaY - 5 >= pos_y and pelotaY  -5 <= pos_y + 100):
        if(pelotaX == 85):
            speedPelotaX *= -1
            #print(f"x: {pelotaX}, y: {pelotaY}")
    if(pelotaX == 29):
        pelotaX = 400 
        contador1 += 1
        if(contador1 < 5):
            texto(screen, blanco, 400, 200, 30, "Jugador 2 a anotado!!", consolas)  
            refresh_screen(clock, 60)
            pygame.time.delay(1000)
        

    pelotaX += speedPelotaX
    pelotaY += speedPelotaY
    #print(f"x: 20, y: {pos_y}")
    pygame.draw.circle(screen, blanco, (pelotaX, pelotaY), 10)
    rectangulo1(screen, blanco, 70, pos_y, 100, 20)
    
    
    refresh_screen(clock, 60)

texto(screen, blanco, 400, 200, 30, "FIN DE JUEGO", consolas)  
refresh_screen(clock, 60)
pygame.time.delay(1000)




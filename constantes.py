import pygame, sys

size = (800,500)
#colores
negro = (0, 0, 0)
blanco = (255, 255, 255)
azul =(0, 0, 255)
verde =(0, 255, 0)
rojo = (255, 0, 0)

cieloNoche = (3, 3, 42)
cieloClaro = (26, 93, 156)
raqueta1 = (29, 15, 148)
#fisicas
speed = 10
speedPelotaX = 7
speedPelotaY = 7
#fuentes
consolas = pygame.font.match_font('consolas')

#funciones
def close_verify():
    #recorriendo todos los eventos de la ventana 
    for event in pygame.event.get():
        #evaluando si el evento es cerrar la ventana
        if event.type == pygame.QUIT:
            #cerrando programa 
            sys.exit()

def refresh_screen(clock, fps):
    pygame.display.flip() 
    clock.tick(fps)     


import pygame, sys

def raqueta(screen, color, x, y, largo, ancho):
    pygame.draw.rect(screen, color, (x, y,ancho, largo))
def pelota(screen, color, x, y, radio):
    pygame.draw.circle(screen, color, (x, y),radio)
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

#Importar pygame y las clases necesarias
import pygame, sys
from pygame.locals import *

#Inicalizar pygame
pygame.init()

#Creación de una ventana para el juego
ventana = pygame.display.set_mode((700, 400))

# Establecer título a la ventana
pygame.display.set_caption('Asteroides☄️')

# Establecer colo de fono de la ventada con rgb
colorFondo = (250, 126, 16)

# Establecer colores de los objetos
colorLinea = (133, 88, 59)
colorCirculo = (153, 105, 74)
colorFigurasEstandar = (169, 167, 165)


# Bucle que mantiene la ventana abierta
while True:
    # Agregar los objetos a la ventana 
    # Establecer el colo de fondo
    ventana.fill(colorFondo)
    
    # Agregar una linea
    pygame.draw.line(ventana, colorLinea, (60, 90), (240, 90), 10)
    #Agregar un circulo
    pygame.draw.circle(ventana, colorCirculo, (100, 200), 70, 10)
    # Agregar poligonos
    #Rectangulo o cuadrado
    pygame.draw.rect(ventana, colorFigurasEstandar, (250, 150, 200, 70))
    pygame.draw.polygon(ventana, colorFigurasEstandar, ((250, 300), (300, 300), (300, 200), (400, 300)))
    
    # Bucle para recorrer cada evento que suceda dentro del juego
    for evento in pygame.event.get():
        # Validar si se presiona X de la ventana
        if evento.type == QUIT:
            # Detener todo
            pygame.quit()
            
            # Cerrar la ventana
            sys.exit()
        
        # Mantener actualizada la ventana
        pygame.display.update()
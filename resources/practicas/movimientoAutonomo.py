#Importar pygame y las clases necesarias
import pygame, sys
from pygame.locals import *
from random import randint

#Inicalizar pygame
pygame.init()

#Creación de una ventana para el juego
ventana = pygame.display.set_mode((700, 500))

# Establecer título a la ventana
pygame.display.set_caption('Asteroides☄️')

# Establecer colo de fono de la ventada con rgb
colorFondo = (250, 126, 16)

# Colores de los objetos
colorFigurasEstandar = (169, 167, 165)

# Variables de movimiento
velocidad = 0.3
direccion = True
posX, posY = randint(1, 700), randint(1, 500)

# Bucle que mantiene la ventana abierta
while True:
    # Agregar los objetos a la ventana 
    # Establecer el colo de fondo
    ventana.fill(colorFondo)
    
    pygame.draw.rect(ventana, colorFigurasEstandar, (posX, posY, 40, 40))
    
    # Eventos de movimiento autonomo
    if direccion == True:
        if posX < (700-40):
            posX += velocidad
        else:
            direccion = False
    else:
        if posX > 1:
            posX -= velocidad
        else:
            direccion = True
    
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
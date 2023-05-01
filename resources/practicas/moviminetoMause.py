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
velocidad = 10
direccion = True
posX, posY = randint(40, 700), randint(40, 500)
lados = 40

# Bucle que mantiene la ventana abierta
while True:
    # Agregar los objetos a la ventana 
    # Establecer el colo de fondo
    ventana.fill(colorFondo)
    
    pygame.draw.rect(ventana, colorFigurasEstandar, (posX, posY, lados, lados))
    
    # Eventos de movimiento por el mause
    posX, posY = pygame.mouse.get_pos()
    posX = posX - (lados / 2)
    posY = posY - (lados / 2)
    
    if posX <= 40: 
        posX = 40
    elif posX >= 620:
        posX = 620
        
    if posY <= 40:
        posY = 40
    elif posY >= 420:
        posY = 420
        
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